"""Uploads above the direct upload limit.

`sources.ingest_file` sends a file larger than `DIRECT_UPLOAD_MAX_BYTES` to an
upload session instead of a single request: it creates the session, sends the
bytes to the session's upload URL in chunks, resuming after a failure, and
completes it. The call returns what the direct request returns.

The upload URL needs no other credential, so it never goes in a log or an
error, and the client's headers never go to it.
"""

from __future__ import annotations

import io
import os
import time
import base64
import random
import hashlib
import pathlib
import tempfile
from typing import IO, TYPE_CHECKING, Any, Dict, Mapping, Callable, Optional, cast
from urllib.parse import urlsplit, urlunsplit

import anyio
import httpx

from ._types import Body, FileTypes, RequestOptions
from ._models import BaseModel
from ._constants import RAW_RESPONSE_HEADER, OVERRIDE_CAST_TO_HEADER
from ._exceptions import UploadError, APIStatusError, APIConnectionError
from ._base_client import make_request_options
from ._utils._sync import to_thread

if TYPE_CHECKING:
    from .resources.sources import SourcesResource, AsyncSourcesResource

__all__ = ["DIRECT_UPLOAD_MAX_BYTES", "prepare_upload"]

_MIB = 1024 * 1024
_CHUNK_UNIT = 256 * 1024

DIRECT_UPLOAD_MAX_BYTES = 30 * _MIB
"""Files up to this size go in one request, as before."""

DIRECT_FALLBACK_MAX_BYTES = 31 * _MIB
"""Up to this size a file can still go in one request if a session fails."""

UPLOAD_MAX_ATTEMPTS = 5
"""Attempts per chunk without progress, and the minimum for complete."""

COMPLETE_DEADLINE_SECONDS = 900.0
"""How long complete may wait on another attempt or a busy server."""

BODY_WATCHDOG_SECONDS = 60.0
"""A complete that sends nothing for this long is retried."""

_MAX_CHUNK_SIZE = 64 * _MIB
_CREATE_PATH = "/sources/upload-sessions"
_COMPLETE_PATH = "/sources/upload-sessions/complete"
_NOT_FOUND_BODY = {"detail": "Not Found"}


class _UploadSession(BaseModel):
    upload_id: str
    build_id: str
    upload_url: str
    chunk_size: int


class UploadSource:
    """A file whose size is known, read in slices from any offset."""

    def __init__(
        self,
        *,
        name: str,
        size: int,
        read_at: Callable[[int, int], bytes],
        close: Optional[Callable[[], None]] = None,
    ) -> None:
        self.name = name
        self.size = size
        self._read_at = read_at
        self._close = close

    def read(self, offset: int, length: int) -> bytes:
        return self._read_at(offset, length)

    def close(self) -> None:
        if self._close is not None:
            self._close()


def _base_name(obj: object, default: str = "upload") -> str:
    name = getattr(obj, "name", None)
    if isinstance(name, (str, os.PathLike)):
        return pathlib.Path(os.fspath(name)).name or default
    return default


def _read_full(stream: IO[bytes], length: int) -> bytes:
    parts: list[bytes] = []
    remaining = length
    while remaining > 0:
        data = stream.read(remaining)
        if not data:
            break
        parts.append(data)
        remaining -= len(data)
    return b"".join(parts)


def _stream_source(stream: IO[bytes], name: str, size: int, close: Optional[Callable[[], None]]) -> UploadSource:
    def read_at(offset: int, length: int) -> bytes:
        stream.seek(offset)
        return _read_full(stream, length)

    return UploadSource(name=name, size=size, read_at=read_at, close=close)


def _seekable_size(stream: IO[bytes]) -> Optional[int]:
    try:
        return os.fstat(stream.fileno()).st_size
    except (OSError, AttributeError, io.UnsupportedOperation):
        pass
    try:
        position = stream.tell()
        size = stream.seek(0, os.SEEK_END)
        stream.seek(position)
        return size
    except (OSError, io.UnsupportedOperation):
        return None


def _content_source(content: object, name: Optional[str]) -> tuple[object, Optional[UploadSource]]:
    """`(content for the direct request, source when above the limit)`."""
    if isinstance(content, bytes):
        if len(content) <= DIRECT_UPLOAD_MAX_BYTES:
            return content, None
        data = content
        return content, UploadSource(
            name=name or "upload", size=len(data), read_at=lambda offset, length: data[offset : offset + length]
        )

    if isinstance(content, os.PathLike):
        path = pathlib.Path(cast("os.PathLike[str]", content))
        size = path.stat().st_size
        if size <= DIRECT_UPLOAD_MAX_BYTES:
            return cast(object, content), None
        opened = path.open("rb")
        return cast(object, content), _stream_source(opened, name or path.name, size, opened.close)

    if isinstance(content, io.IOBase):
        stream = cast(IO[bytes], content)
        file_name = name or _base_name(stream)
        if stream.seekable():
            stream_size = _seekable_size(stream)
            if stream_size is None or stream_size <= DIRECT_UPLOAD_MAX_BYTES:
                return content, None
            # Uploaded from the start, as the direct request does.
            return content, _stream_source(stream, file_name, stream_size, None)

        # Not seekable: its size is only known by reading it, so it is spooled.
        spool = tempfile.TemporaryFile()
        while True:
            block = stream.read(8 * _MIB)
            if not block:
                break
            spool.write(block)
        size = spool.tell()
        spool.seek(0)
        if size <= DIRECT_UPLOAD_MAX_BYTES:
            return (file_name, spool), None
        return (file_name, spool), _stream_source(cast(IO[bytes], spool), file_name, size, spool.close)

    return content, None


def prepare_upload(file: FileTypes) -> tuple[FileTypes, Optional[UploadSource]]:
    """Measure `file`: what the direct request would send, and a source when
    the file is above the direct upload limit."""
    if isinstance(file, tuple):
        if len(file) < 2 or not file[0]:
            return file, None
        direct_content, source = _content_source(file[1], str(file[0]))
        return cast(FileTypes, (file[0], direct_content, *file[2:])), source

    direct, source = _content_source(file, None)
    return cast(FileTypes, direct), source


def rewind(file: FileTypes) -> None:
    """Put a file object back at its start before the direct request."""
    content = file[1] if isinstance(file, tuple) and len(file) > 1 else file
    if isinstance(content, io.IOBase) and content.seekable():
        content.seek(0)


# ---------------------------------------------------------------------------
# Shared rules
# ---------------------------------------------------------------------------


def _create_options(
    extra_headers: Optional[Mapping[str, Any]],
    extra_query: Optional[Mapping[str, object]],
    extra_body: Optional[Body],
    timeout: Any,
) -> RequestOptions:
    # Create returns the session, never the caller's raw or streamed response.
    headers = {
        k: v
        for k, v in (extra_headers or {}).items()
        if k not in (RAW_RESPONSE_HEADER, OVERRIDE_CAST_TO_HEADER) and k.lower() != "content-type"
    }
    return make_request_options(extra_headers=headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout)


def _create_body(source: UploadSource, method: object, enrichment: object, indexing: object) -> Dict[str, object]:
    body: Dict[str, object] = {"file_name": source.name, "file_size": source.size}
    for key, value in (("method", method), ("enrichment", enrichment), ("indexing", indexing)):
        if value is not None and not _is_omitted(value):
            body[key] = value
    return body


def _is_omitted(value: object) -> bool:
    from ._types import Omit, NotGiven

    return isinstance(value, (Omit, NotGiven))


def falls_back(error: Exception, size: int) -> bool:
    """Whether a failed session start should send the file directly."""
    if size <= DIRECT_FALLBACK_MAX_BYTES:
        return True
    if isinstance(error, APIStatusError):
        if error.status_code == 501:
            return True
        # A server without sessions answers the framework's own 404.
        return error.status_code == 404 and error.body == _NOT_FOUND_BODY
    return False


def _check_session(session: _UploadSession) -> None:
    if urlsplit(session.upload_url).scheme != "https":
        raise UploadError("The upload URL is not https.", request=_scrubbed_request("PUT", ""), offset=0)
    size = session.chunk_size
    if size <= 0 or size % _CHUNK_UNIT or size > _MAX_CHUNK_SIZE:
        raise UploadError("The upload chunk size is not valid.", request=_scrubbed_request("PUT", ""), offset=0)


def _scrubbed_request(method: str, url: str) -> httpx.Request:
    """A request for an error, without the URL's query, which holds the session."""
    parts = urlsplit(url)
    return httpx.Request(method, urlunsplit((parts.scheme or "https", parts.netloc or "storage", parts.path, "", "")))


def _new_md5() -> Any:
    try:
        return hashlib.md5(usedforsecurity=False)  # type: ignore[call-arg]
    except (TypeError, ValueError):  # TypeError: Python without the flag
        try:
            return hashlib.md5()
        except ValueError:  # FIPS: no MD5, so none is sent
            return None


def _put_timeout(timeout: Any, client_timeout: Any) -> Dict[str, Optional[float]]:
    chosen = client_timeout if timeout is None or _is_omitted(timeout) else timeout
    if isinstance(chosen, httpx.Timeout):
        timeouts = chosen.as_dict()
    else:
        timeouts = httpx.Timeout(chosen).as_dict()
    return {key: value for key, value in timeouts.items()}


def _complete_timeout(timeout: Any, client_timeout: Any) -> httpx.Timeout:
    # Its read timeout is the body watchdog: a complete heartbeats every 15 s.
    chosen = client_timeout if timeout is None or _is_omitted(timeout) else timeout
    base = chosen if isinstance(chosen, httpx.Timeout) else httpx.Timeout(chosen)
    return httpx.Timeout(connect=base.connect, read=BODY_WATCHDOG_SECONDS, write=base.write, pool=base.pool)


def _backoff(attempt: int) -> float:
    return float(min(0.5 * 2.0**attempt, 8.0) * (1 - 0.25 * random.random()))


def _retry_after(headers: Mapping[str, str]) -> Optional[float]:
    value = headers.get("retry-after")
    try:
        return float(value) if value is not None else None
    except ValueError:
        return None


class _ChunkState:
    """The upload protocol, without I/O: what to send next after each answer."""

    def __init__(self, source: UploadSource, chunk_size: int) -> None:
        self.source = source
        self.chunk_size = chunk_size
        self.offset = 0
        self.sent_upto = 0
        self.hashed_upto = 0
        self.attempts = 0
        self.done = False
        self.md5 = _new_md5()

    def next_chunk(self) -> tuple[int, int]:
        return self.offset, min(self.offset + self.chunk_size, self.source.size)

    def read_and_hash(self, start: int, end: int) -> bytes:
        data = self.source.read(start, end - start)
        if len(data) != end - start:
            raise UploadError(
                "The file changed while it was being uploaded.", request=_scrubbed_request("PUT", ""), offset=start
            )
        # Only bytes past the hashed point: a resume re-reads part of a chunk.
        if self.md5 is not None and end > self.hashed_upto:
            self.md5.update(data[self.hashed_upto - start :] if self.hashed_upto > start else data)
            self.hashed_upto = end
        self.sent_upto = max(self.sent_upto, end)
        return data

    def persisted(self, response: httpx.Response) -> Optional[int]:
        """The next offset from a `308`, or None when the upload is done."""
        if response.status_code in (200, 201):
            return None
        rng = response.headers.get("range")
        if not rng:
            return 0
        try:
            return int(rng.rsplit("-", 1)[1]) + 1
        except (IndexError, ValueError):
            return 0

    def advance(self, new_offset: Optional[int], url: str) -> None:
        if new_offset is None:
            self.done = True
            self.offset = self.source.size
            return
        if new_offset > self.sent_upto or new_offset > self.source.size:
            raise UploadError(
                "The upload reported more bytes than were sent.",
                request=_scrubbed_request("PUT", url),
                offset=new_offset,
            )
        if new_offset > self.offset:
            self.attempts = 0
        else:
            self.attempts += 1
        self.offset = new_offset

    def give_up(self) -> bool:
        return self.attempts >= UPLOAD_MAX_ATTEMPTS

    def digest(self) -> Optional[str]:
        if self.md5 is None or self.hashed_upto != self.source.size:
            return None
        return base64.b64encode(self.md5.digest()).decode()


def _is_transient(status: int) -> bool:
    return status in (408, 429) or status >= 500


def _session_lost(status: int) -> bool:
    return status in (404, 410)


class _Verdict:
    """How complete goes on after one attempt."""

    FREE = "free"  # wait, without spending an attempt
    RETRY = "retry"
    FINAL = "final"


def _status_verdict(status: int, headers: Mapping[str, str]) -> str:
    if headers.get("x-conversion-busy") == "true" or (status == 409 and headers.get("retry-after")):
        return _Verdict.FREE
    should_retry = headers.get("x-should-retry")
    if should_retry is not None:
        return _Verdict.RETRY if should_retry == "true" else _Verdict.FINAL
    return _Verdict.RETRY if status in (408, 409, 429) or status >= 500 else _Verdict.FINAL


def _envelope_verdict(data: Mapping[str, Any]) -> str:
    if data.get("busy"):
        return _Verdict.FREE
    return _Verdict.RETRY if data.get("retryable") else _Verdict.FINAL


def _envelope_error(client: Any, data: Mapping[str, Any], response: httpx.Response) -> APIStatusError:
    status = data.get("status_code")
    status = status if isinstance(status, int) and status >= 400 else 500
    fake = httpx.Response(status, request=response.request, headers=response.headers, json=dict(data))
    return cast(
        APIStatusError,
        client._make_status_error(str(data.get("detail") or "Upload failed"), body=dict(data), response=fake),
    )


def _complete_options(
    extra_headers: Optional[Mapping[str, Any]], extra_query: Optional[Mapping[str, object]], timeout: httpx.Timeout
) -> RequestOptions:
    headers = {k: v for k, v in (extra_headers or {}).items() if k.lower() != "content-type"}
    headers[RAW_RESPONSE_HEADER] = "true"
    options = make_request_options(extra_headers=headers, extra_query=extra_query, timeout=timeout)
    options["max_retries"] = 0  # complete runs its own loop
    return options


# ---------------------------------------------------------------------------
# Sync
# ---------------------------------------------------------------------------


def upload(
    resource: "SourcesResource",
    source: UploadSource,
    *,
    direct: Callable[[], Any],
    method: object,
    enrichment: object,
    indexing: object,
    extra_headers: Optional[Mapping[str, Any]],
    extra_query: Optional[Mapping[str, object]],
    extra_body: Optional[Body],
    timeout: Any,
) -> Any:
    client = resource._client
    try:
        try:
            session = resource._post(
                _CREATE_PATH,
                body=_create_body(source, method, enrichment, indexing),
                options=_create_options(extra_headers, extra_query, extra_body, timeout),
                cast_to=_UploadSession,
            )
        except (APIStatusError, APIConnectionError) as e:
            if falls_back(e, source.size):
                return direct()
            raise
        _check_session(session)
        try:
            md5 = _send_chunks(client, session, source, timeout)
        except UploadError:
            if source.size <= DIRECT_FALLBACK_MAX_BYTES:
                return direct()
            raise
        return _complete(resource, session, md5, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout)
    finally:
        source.close()


def _put(client: Any, url: str, body: bytes, content_range: str, timeout: Dict[str, Optional[float]]) -> httpx.Response:
    # The client's transport, so proxies and certificates still apply, but a
    # bare request: no client header, no auth, no redirect.
    request = httpx.Request(
        "PUT",
        url,
        headers={"Content-Range": content_range, "Content-Length": str(len(body))},
        content=body,
        extensions={"timeout": timeout},
    )
    return cast(httpx.Response, client._client.send(request, auth=None, follow_redirects=False))


def _send_chunks(client: Any, session: _UploadSession, source: UploadSource, timeout: Any) -> Optional[str]:
    url = session.upload_url
    put_timeout = _put_timeout(timeout, client.timeout)
    state = _ChunkState(source, session.chunk_size)
    status: Optional[int] = None
    while not state.done:
        start, end = state.next_chunk()
        data = state.read_and_hash(start, end)
        response: Optional[httpx.Response] = None
        try:
            response = _put(client, url, data, f"bytes {start}-{end - 1}/{source.size}", put_timeout)
            response.read()
            status = response.status_code
        except httpx.TransportError:
            response = None

        if response is not None and (status in (200, 201, 308)):
            state.advance(state.persisted(response), url)
            continue
        if response is not None and status is not None and _session_lost(status):
            raise UploadError(
                "The upload session expired or was lost.",
                request=_scrubbed_request("PUT", url),
                offset=start,
                status_code=status,
            )
        if response is not None and status is not None and not _is_transient(status):
            raise UploadError(
                "The upload was rejected.", request=_scrubbed_request("PUT", url), offset=start, status_code=status
            )

        delay = (_retry_after(response.headers) if response is not None else None) or _backoff(state.attempts)
        time.sleep(delay)
        new_offset: Optional[int] = state.offset
        try:
            query = _put(client, url, b"", f"bytes */{source.size}", put_timeout)
            query.read()
            if query.status_code in (200, 201, 308):
                new_offset = state.persisted(query)
            elif _session_lost(query.status_code):
                raise UploadError(
                    "The upload session expired or was lost.",
                    request=_scrubbed_request("PUT", url),
                    offset=start,
                    status_code=query.status_code,
                )
        except httpx.TransportError:
            pass
        state.advance(new_offset, url)
        if not state.done and state.give_up():
            raise UploadError(
                "The upload failed after several attempts.",
                request=_scrubbed_request("PUT", url),
                offset=state.offset,
                status_code=status,
            )
    return state.digest()


def _complete(
    resource: "SourcesResource",
    session: _UploadSession,
    md5: Optional[str],
    *,
    extra_headers: Optional[Mapping[str, Any]],
    extra_query: Optional[Mapping[str, object]],
    timeout: Any,
) -> Any:
    client = resource._client
    body: Dict[str, object] = {"upload_id": session.upload_id}
    if md5 is not None:
        body["md5"] = md5
    raw_mode = (extra_headers or {}).get(RAW_RESPONSE_HEADER)
    if raw_mode == "stream":
        # The caller reads the body, so this is one plain attempt.
        return resource._post(
            _COMPLETE_PATH,
            body=body,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, timeout=timeout),
            cast_to=_ingest_response_type(),
        )

    budget = max(int(client.max_retries), UPLOAD_MAX_ATTEMPTS)
    options = _complete_options(extra_headers, extra_query, _complete_timeout(timeout, client.timeout))
    attempts = 0
    waited = 0.0
    last: Optional[Exception] = None
    while True:
        delay: Optional[float] = None
        verdict = _Verdict.RETRY
        try:
            raw = resource._post(_COMPLETE_PATH, body=body, options=options, cast_to=_ingest_response_type())
            data = cast(object, raw.json())
            waited = 0.0
            if isinstance(data, dict) and cast(Dict[str, Any], data).get("build_id"):
                return raw if raw_mode else raw.parse()
            if isinstance(data, dict) and "status_code" in data:
                envelope = cast(Dict[str, Any], data)
                verdict = _envelope_verdict(envelope)
                last = _envelope_error(client, envelope, raw.http_response)
                delay = cast(Optional[float], envelope.get("retry_after"))
                if verdict == _Verdict.FINAL:
                    raise last
            else:
                last = None
        except APIStatusError as e:
            if e is last:
                raise
            verdict = _status_verdict(e.status_code, e.response.headers)
            if verdict == _Verdict.FINAL:
                raise
            last = e
            delay = _retry_after(e.response.headers)
        except (APIConnectionError, httpx.HTTPError) as e:
            last = e

        if verdict == _Verdict.FREE:
            delay = delay or 20.0
            waited += delay
            if waited > COMPLETE_DEADLINE_SECONDS:
                raise _gave_up(session, last)
        else:
            attempts += 1
            if attempts >= budget:
                if isinstance(last, APIStatusError):
                    raise last
                raise _gave_up(session, last)
            delay = delay or _backoff(attempts)
        time.sleep(delay)


def _gave_up(session: _UploadSession, last: Optional[Exception]) -> UploadError:
    error = UploadError(
        "The upload was sent but could not be completed. Check the build before uploading again.",
        request=_scrubbed_request("POST", ""),
        offset=-1,
        build_id=session.build_id,
    )
    error.__cause__ = last
    return error


def _ingest_response_type() -> Any:
    from .types.source_ingest_file_response import SourceIngestFileResponse

    return SourceIngestFileResponse


# ---------------------------------------------------------------------------
# Async: the same steps, with file work in a thread.
# ---------------------------------------------------------------------------


async def async_prepare_upload(file: FileTypes) -> tuple[FileTypes, Optional[UploadSource]]:
    return await to_thread(prepare_upload, file)


async def async_upload(
    resource: "AsyncSourcesResource",
    source: UploadSource,
    *,
    direct: Callable[[], Any],
    method: object,
    enrichment: object,
    indexing: object,
    extra_headers: Optional[Mapping[str, Any]],
    extra_query: Optional[Mapping[str, object]],
    extra_body: Optional[Body],
    timeout: Any,
) -> Any:
    client = resource._client
    try:
        try:
            session = await resource._post(
                _CREATE_PATH,
                body=_create_body(source, method, enrichment, indexing),
                options=_create_options(extra_headers, extra_query, extra_body, timeout),
                cast_to=_UploadSession,
            )
        except (APIStatusError, APIConnectionError) as e:
            if falls_back(e, source.size):
                return await direct()
            raise
        _check_session(session)
        try:
            md5 = await _async_send_chunks(client, session, source, timeout)
        except UploadError:
            if source.size <= DIRECT_FALLBACK_MAX_BYTES:
                return await direct()
            raise
        return await _async_complete(
            resource, session, md5, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout
        )
    finally:
        await to_thread(source.close)


async def _async_put(
    client: Any, url: str, body: bytes, content_range: str, timeout: Dict[str, Optional[float]]
) -> httpx.Response:
    request = httpx.Request(
        "PUT",
        url,
        headers={"Content-Range": content_range, "Content-Length": str(len(body))},
        content=body,
        extensions={"timeout": timeout},
    )
    response = await client._client.send(request, auth=None, follow_redirects=False)
    await response.aread()
    return cast(httpx.Response, response)


async def _async_send_chunks(client: Any, session: _UploadSession, source: UploadSource, timeout: Any) -> Optional[str]:
    url = session.upload_url
    put_timeout = _put_timeout(timeout, client.timeout)
    state = _ChunkState(source, session.chunk_size)
    status: Optional[int] = None
    while not state.done:
        start, end = state.next_chunk()
        data = await to_thread(state.read_and_hash, start, end)
        response: Optional[httpx.Response] = None
        try:
            response = await _async_put(client, url, data, f"bytes {start}-{end - 1}/{source.size}", put_timeout)
            status = response.status_code
        except httpx.TransportError:
            response = None

        if response is not None and status in (200, 201, 308):
            state.advance(state.persisted(response), url)
            continue
        if response is not None and status is not None and _session_lost(status):
            raise UploadError(
                "The upload session expired or was lost.",
                request=_scrubbed_request("PUT", url),
                offset=start,
                status_code=status,
            )
        if response is not None and status is not None and not _is_transient(status):
            raise UploadError(
                "The upload was rejected.", request=_scrubbed_request("PUT", url), offset=start, status_code=status
            )

        await anyio.sleep(
            (_retry_after(response.headers) if response is not None else None) or _backoff(state.attempts)
        )
        new_offset: Optional[int] = state.offset
        try:
            query = await _async_put(client, url, b"", f"bytes */{source.size}", put_timeout)
            if query.status_code in (200, 201, 308):
                new_offset = state.persisted(query)
            elif _session_lost(query.status_code):
                raise UploadError(
                    "The upload session expired or was lost.",
                    request=_scrubbed_request("PUT", url),
                    offset=start,
                    status_code=query.status_code,
                )
        except httpx.TransportError:
            pass
        state.advance(new_offset, url)
        if not state.done and state.give_up():
            raise UploadError(
                "The upload failed after several attempts.",
                request=_scrubbed_request("PUT", url),
                offset=state.offset,
                status_code=status,
            )
    return state.digest()


async def _async_complete(
    resource: "AsyncSourcesResource",
    session: _UploadSession,
    md5: Optional[str],
    *,
    extra_headers: Optional[Mapping[str, Any]],
    extra_query: Optional[Mapping[str, object]],
    timeout: Any,
) -> Any:
    client = resource._client
    body: Dict[str, object] = {"upload_id": session.upload_id}
    if md5 is not None:
        body["md5"] = md5
    raw_mode = (extra_headers or {}).get(RAW_RESPONSE_HEADER)
    if raw_mode == "stream":
        return await resource._post(
            _COMPLETE_PATH,
            body=body,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, timeout=timeout),
            cast_to=_ingest_response_type(),
        )

    budget = max(int(client.max_retries), UPLOAD_MAX_ATTEMPTS)
    options = _complete_options(extra_headers, extra_query, _complete_timeout(timeout, client.timeout))
    attempts = 0
    waited = 0.0
    last: Optional[Exception] = None
    while True:
        delay: Optional[float] = None
        verdict = _Verdict.RETRY
        try:
            raw = await resource._post(_COMPLETE_PATH, body=body, options=options, cast_to=_ingest_response_type())
            data = cast(object, await raw.json())
            waited = 0.0
            if isinstance(data, dict) and cast(Dict[str, Any], data).get("build_id"):
                return raw if raw_mode else await raw.parse()
            if isinstance(data, dict) and "status_code" in data:
                envelope = cast(Dict[str, Any], data)
                verdict = _envelope_verdict(envelope)
                last = _envelope_error(client, envelope, raw.http_response)
                delay = cast(Optional[float], envelope.get("retry_after"))
                if verdict == _Verdict.FINAL:
                    raise last
            else:
                last = None
        except APIStatusError as e:
            if e is last:
                raise
            verdict = _status_verdict(e.status_code, e.response.headers)
            if verdict == _Verdict.FINAL:
                raise
            last = e
            delay = _retry_after(e.response.headers)
        except (APIConnectionError, httpx.HTTPError) as e:
            last = e

        if verdict == _Verdict.FREE:
            delay = delay or 20.0
            waited += delay
            if waited > COMPLETE_DEADLINE_SECONDS:
                raise _gave_up(session, last)
        else:
            attempts += 1
            if attempts >= budget:
                if isinstance(last, APIStatusError):
                    raise last
                raise _gave_up(session, last)
            delay = delay or _backoff(attempts)
        await anyio.sleep(delay)
