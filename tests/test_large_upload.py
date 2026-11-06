"""`sources.ingest_file` for files above the direct upload limit, against a
fake API and a fake resumable upload URL."""

from __future__ import annotations

import io
import json
import base64
import hashlib
import logging
from types import SimpleNamespace
from typing import Any, Dict, List, Callable, Optional, cast
from pathlib import Path
from typing_extensions import override

import httpx
import pytest

import graphor._large_upload as large
from graphor import Graphor, UploadError, AsyncGraphor, NotFoundError, UnprocessableEntityError

KIB = 1024
CHUNK = 256 * KIB
BASE_URL = "https://api.example.test/v1"
UPLOAD_URL = "https://storage.example.test/upload/session?upload_id=secret-session"


class FakeServer:
    """The API's three routes and a resumable upload URL."""

    def __init__(self) -> None:
        self.create_status = 201
        self.create_body: Any = None
        self.chunk_size = CHUNK
        self.upload_url = UPLOAD_URL
        self.stored = bytearray()
        self.size = 0
        self.finished = False
        self.requests: List[httpx.Request] = []
        self.direct_calls = 0
        self.create_calls: List[Dict[str, Any]] = []
        self.complete_bodies: List[Dict[str, Any]] = []
        # Hooks: return a response or raise to replace the default behaviour.
        self.on_put: Optional[Callable[[int, int, bytes], Optional[httpx.Response]]] = None
        self.complete_script: List[Callable[[], httpx.Response]] = []

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        url = str(request.url)
        if url.startswith("https://storage.example.test"):
            return self._storage(request)
        if request.url.path.endswith("/sources/upload-sessions"):
            body = json.loads(request.content)
            self.create_calls.append(body)
            if self.create_status != 201:
                return httpx.Response(self.create_status, json=self.create_body or {"detail": "no"})
            self.size = body["file_size"]
            return httpx.Response(
                201,
                json={
                    "upload_id": "token",
                    "build_id": "bid",
                    "upload_url": self.upload_url,
                    "chunk_size": self.chunk_size,
                    "expires_at": "2030-01-01T00:00:00Z",
                },
            )
        if request.url.path.endswith("/upload-sessions/complete"):
            self.complete_bodies.append(json.loads(request.content))
            if self.complete_script:
                return self.complete_script.pop(0)()
            return httpx.Response(200, json={"build_id": "bid", "success": True})
        if request.url.path.endswith("/sources/ingest-file"):
            self.direct_calls += 1
            return httpx.Response(200, json={"build_id": "direct", "success": True})
        return httpx.Response(404, json={"detail": "Not Found"})

    def _storage(self, request: httpx.Request) -> httpx.Response:
        rng = request.headers["content-range"]
        if rng.startswith("bytes */"):
            return self._status()
        span, total = rng[len("bytes ") :].split("/")
        start, end = (int(x) for x in span.split("-"))
        body = request.content
        if self.on_put is not None:
            replaced = self.on_put(start, end, body)
            if replaced is not None:
                return replaced
        if start == len(self.stored):
            self.stored += body
        if len(self.stored) >= int(total):
            self.finished = True
            return httpx.Response(200, json={"size": len(self.stored)})
        return self._status()

    def _status(self) -> httpx.Response:
        if self.finished:
            return httpx.Response(200, json={})
        if not self.stored:
            return httpx.Response(308)
        return httpx.Response(308, headers={"Range": f"bytes=0-{len(self.stored) - 1}"})

    def md5(self) -> str:
        return base64.b64encode(hashlib.md5(bytes(self.stored)).digest()).decode()


@pytest.fixture(autouse=True)
def small_limits(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(large, "DIRECT_UPLOAD_MAX_BYTES", 100 * KIB)
    monkeypatch.setattr(large, "DIRECT_FALLBACK_MAX_BYTES", 200 * KIB)

    def no_wait(_s: float) -> None:
        return None

    monkeypatch.setattr(large, "time", SimpleNamespace(sleep=no_wait))

    async def no_sleep(_s: float) -> None:
        return None

    monkeypatch.setattr(large, "anyio", SimpleNamespace(sleep=no_sleep))


@pytest.fixture
def server() -> FakeServer:
    return FakeServer()


def _client(server: FakeServer, **kwargs: Any) -> Graphor:
    return Graphor(
        api_key="test-key",
        base_url=BASE_URL,
        default_headers={"X-Custom": "client-header"},
        http_client=httpx.Client(transport=httpx.MockTransport(server.handler)),
        **kwargs,
    )


def _async_client(server: FakeServer) -> AsyncGraphor:
    return AsyncGraphor(
        api_key="test-key",
        base_url=BASE_URL,
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(server.handler)),
    )


def _data(size: int = 600 * KIB) -> bytes:
    return bytes((i * 7 + 3) % 251 for i in range(size))


def _puts(server: FakeServer) -> List[httpx.Request]:
    return [r for r in server.requests if str(r.url).startswith("https://storage.example.test")]


# --- which path --------------------------------------------------------------


def test_a_small_file_goes_directly(server: FakeServer) -> None:
    result = _client(server).sources.ingest_file(file=("a.pdf", _data(50 * KIB)))
    assert result.build_id == "direct"
    assert server.create_calls == [] and server.direct_calls == 1


def test_a_large_file_goes_through_a_session(server: FakeServer, tmp_path: Path) -> None:
    data = _data()
    path = tmp_path / "Report.PDF"
    path.write_bytes(data)
    result = _client(server).sources.ingest_file(file=path, method="fast")

    assert result.build_id == "bid"
    assert bytes(server.stored) == data
    assert server.create_calls == [{"file_name": "Report.PDF", "file_size": len(data), "method": "fast"}]
    assert server.complete_bodies == [{"upload_id": "token", "md5": server.md5()}]
    assert server.direct_calls == 0


def test_no_client_header_reaches_the_upload_url(server: FakeServer) -> None:
    _client(server).sources.ingest_file(file=("a.pdf", _data()), extra_headers={"X-Extra": "1"})
    for request in _puts(server):
        names = {name.lower() for name in request.headers}
        assert "authorization" not in names and "x-custom" not in names and "x-extra" not in names
        assert not any(name.startswith("x-stainless") for name in names)
        assert "content-range" in names


def test_a_file_opened_from_a_path_sends_its_base_name(server: FakeServer, tmp_path: Path) -> None:
    path = tmp_path / "nested" / "big.pdf"
    path.parent.mkdir()
    path.write_bytes(_data())
    with path.open("rb") as f:
        _client(server).sources.ingest_file(file=f)
    assert server.create_calls[0]["file_name"] == "big.pdf"


def test_a_non_seekable_stream_is_spooled(server: FakeServer) -> None:
    data = _data()

    class Pipe(io.RawIOBase):
        def __init__(self) -> None:
            self.inner = io.BytesIO(data)
            self.name = "piped.pdf"

        @override
        def readable(self) -> bool:
            return True

        @override
        def seekable(self) -> bool:
            return False

        @override
        def readinto(self, buffer: Any) -> int:
            chunk = self.inner.read(len(buffer))
            buffer[: len(chunk)] = chunk
            return len(chunk)

    _client(server).sources.ingest_file(file=cast(Any, Pipe()))
    assert bytes(server.stored) == data
    assert server.create_calls[0]["file_name"] == "piped.pdf"


def test_reads_stay_near_one_chunk(server: FakeServer) -> None:
    data = _data()
    largest = 0

    class Counting(io.BytesIO):
        name = "counted.pdf"

        @override
        def read(self, size: Optional[int] = -1) -> bytes:
            nonlocal largest
            chunk = super().read(size)
            largest = max(largest, len(chunk))
            return chunk

    _client(server).sources.ingest_file(file=Counting(data))
    assert 0 < largest <= CHUNK


# --- falling back to the direct request -------------------------------------


@pytest.mark.parametrize(
    ("status", "body"),
    [(501, {"detail": "Upload sessions are not available"}), (404, {"detail": "Not Found"})],
)
def test_no_sessions_falls_back(server: FakeServer, status: int, body: Dict[str, Any]) -> None:
    server.create_status, server.create_body = status, body
    assert _client(server).sources.ingest_file(file=("a.pdf", _data())).build_id == "direct"


def test_another_404_is_raised(server: FakeServer) -> None:
    server.create_status, server.create_body = 404, {"detail": "Project not found"}
    with pytest.raises(NotFoundError):
        _client(server).sources.ingest_file(file=("a.pdf", _data()))
    assert server.direct_calls == 0


def test_near_the_limit_any_failure_falls_back(server: FakeServer) -> None:
    server.create_status = 503
    assert _client(server).sources.ingest_file(file=("a.pdf", _data(150 * KIB))).build_id == "direct"
    server.create_status = 201

    def refuse(_start: int, _end: int, _body: bytes) -> httpx.Response:
        return httpx.Response(403)

    server.on_put = refuse
    assert _client(server).sources.ingest_file(file=("a.pdf", _data(150 * KIB))).build_id == "direct"


# --- the upload protocol ----------------------------------------------------


def test_a_cut_chunk_resumes_with_the_right_md5(server: FakeServer) -> None:
    data = _data()
    cut = {"done": False}

    def cut_once(start: int, _end: int, body: bytes) -> Optional[httpx.Response]:
        if start == CHUNK and not cut["done"]:
            cut["done"] = True
            server.stored += body[: CHUNK // 2]  # half arrived, then the connection dropped
            raise httpx.ReadError("connection reset")
        return None

    server.on_put = cut_once
    _client(server).sources.ingest_file(file=("a.pdf", data))
    assert bytes(server.stored) == data
    assert server.complete_bodies[0]["md5"] == base64.b64encode(hashlib.md5(data).digest()).decode()


def test_a_short_range_resends_from_there(server: FakeServer) -> None:
    data = _data()
    first = {"done": False}

    def keep_half(start: int, _end: int, body: bytes) -> Optional[httpx.Response]:
        if start == 0 and not first["done"]:
            first["done"] = True
            server.stored += body[:KIB]
            return httpx.Response(308, headers={"Range": f"bytes=0-{KIB - 1}"})
        return None

    server.on_put = keep_half
    _client(server).sources.ingest_file(file=("a.pdf", data))
    assert bytes(server.stored) == data


def test_a_503_on_the_last_chunk_then_a_query_saying_done(server: FakeServer) -> None:
    data = _data()

    def last_fails(_start: int, end: int, body: bytes) -> Optional[httpx.Response]:
        if end == len(data) - 1:
            server.stored += body
            server.finished = True
            return httpx.Response(503)
        return None

    server.on_put = last_fails
    assert _client(server).sources.ingest_file(file=("a.pdf", data)).build_id == "bid"


def test_a_lost_session_raises_without_the_url(server: FakeServer, caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG)
    server.on_put = lambda _start, _end, _body: httpx.Response(410)
    with pytest.raises(UploadError) as exc:
        _client(server).sources.ingest_file(file=("a.pdf", _data()))
    assert exc.value.status_code == 410
    assert "secret-session" not in str(exc.value)
    assert "secret-session" not in str(exc.value.request.url)
    # The SDK's own logs; httpx's request line is the caller's to enable.
    assert not any("secret-session" in r.getMessage() for r in caplog.records if r.name.startswith("graphor"))


def test_no_progress_spends_the_budget(server: FakeServer) -> None:
    def never(_start: int, _end: int, _body: bytes) -> httpx.Response:
        raise httpx.ConnectError("down")

    server.on_put = never
    with pytest.raises(UploadError):
        _client(server).sources.ingest_file(file=("a.pdf", _data()))
    puts = [r for r in _puts(server) if not r.headers["content-range"].startswith("bytes */")]
    assert len(puts) == large.UPLOAD_MAX_ATTEMPTS


@pytest.mark.parametrize(
    ("url", "chunk"),
    [
        ("http://storage.example.test/x", CHUNK),
        (UPLOAD_URL, CHUNK + 1),
        (UPLOAD_URL, 0),
        (UPLOAD_URL, 128 * 1024 * 1024),
    ],
)
def test_a_bad_session_raises_before_sending(server: FakeServer, url: str, chunk: int) -> None:
    server.upload_url, server.chunk_size = url, chunk
    with pytest.raises(UploadError):
        _client(server).sources.ingest_file(file=("a.pdf", _data()))
    assert _puts(server) == []


def test_without_md5_nothing_is_sent(server: FakeServer, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(large, "_new_md5", lambda: None)
    _client(server).sources.ingest_file(file=("a.pdf", _data()))
    assert server.complete_bodies == [{"upload_id": "token"}]


# --- complete ----------------------------------------------------------------


def _envelope(status: int, retryable: bool, busy: bool = False) -> Callable[[], httpx.Response]:
    return lambda: httpx.Response(
        200,
        content=b"\n\n"
        + json.dumps(
            {"detail": "x", "status_code": status, "retryable": retryable, "retry_after": 1, "busy": busy}
        ).encode(),
    )


def test_complete_retries_a_retryable_envelope(server: FakeServer) -> None:
    server.complete_script = [_envelope(503, True), _envelope(503, True, busy=True)]
    assert _client(server).sources.ingest_file(file=("a.pdf", _data())).build_id == "bid"
    assert len(server.complete_bodies) == 3


def test_complete_waits_on_a_409_without_spending_attempts(server: FakeServer) -> None:
    conflict = lambda: httpx.Response(409, headers={"Retry-After": "1"}, json={"detail": "busy"})  # noqa: E731
    server.complete_script = [conflict] * 8
    assert _client(server).sources.ingest_file(file=("a.pdf", _data())).build_id == "bid"
    assert len(server.complete_bodies) == 9


def test_complete_raises_a_final_envelope(server: FakeServer) -> None:
    server.complete_script = [_envelope(422, False)]
    with pytest.raises(UnprocessableEntityError):
        _client(server).sources.ingest_file(file=("a.pdf", _data()))
    assert len(server.complete_bodies) == 1


def test_complete_with_no_build_id_gives_up_with_the_build(server: FakeServer) -> None:
    server.complete_script = [lambda: httpx.Response(200, content=b"\n\n{}")] * 10
    with pytest.raises(UploadError) as exc:
        _client(server).sources.ingest_file(file=("a.pdf", _data()))
    assert exc.value.build_id == "bid"
    assert len(server.complete_bodies) == large.UPLOAD_MAX_ATTEMPTS


def test_complete_survives_a_dropped_connection(server: FakeServer) -> None:
    def drop() -> httpx.Response:
        raise httpx.RemoteProtocolError("peer closed connection")

    server.complete_script = [drop]
    assert _client(server).sources.ingest_file(file=("a.pdf", _data())).build_id == "bid"


def test_raw_response_returns_completes_response(server: FakeServer) -> None:
    raw = _client(server).sources.with_raw_response.ingest_file(file=("a.pdf", _data()))
    assert raw.parse().build_id == "bid"
    assert raw.http_response.request.url.path.endswith("/upload-sessions/complete")


# --- async -------------------------------------------------------------------


async def test_async_upload_resumes(server: FakeServer) -> None:
    data = _data()
    cut = {"done": False}

    def cut_once(start: int, _end: int, _body: bytes) -> Optional[httpx.Response]:
        if start == CHUNK and not cut["done"]:
            cut["done"] = True
            raise httpx.ReadError("connection reset")
        return None

    server.on_put = cut_once
    result = await _async_client(server).sources.ingest_file(file=("a.pdf", data))
    assert result.build_id == "bid"
    assert bytes(server.stored) == data
    assert server.complete_bodies[0]["md5"] == server.md5()


async def test_async_small_file_goes_directly(server: FakeServer) -> None:
    result = await _async_client(server).sources.ingest_file(file=("a.pdf", _data(10 * KIB)))
    assert result.build_id == "direct"
