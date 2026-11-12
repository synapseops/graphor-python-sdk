"""Folder parameters: how they are sent, and the checks that the API applied them.

The API echoes every folder filter or scope it applies: `folder` on each
listed source, `folders` on the answers of `ask`, `extract` and
`retrieve_chunks`, and `folder` on an upload session. An API that does not
support folders ignores the parameters, so a call that sent one checks the
echo and raises `FolderScopeNotAppliedError` instead of returning a result
that may cover the whole project.
"""

from __future__ import annotations

from typing import Any, Dict, List, Type, Mapping, TypeVar, Callable, Optional, Sequence, cast

import httpx

from ._types import Omit, NotGiven
from ._models import BaseModel, validate_type, construct_type
from ._exceptions import GraphorError, NotFoundError, FolderScopeNotAppliedError

_M = TypeVar("_M", bound=BaseModel)

__all__ = [
    "is_top_level",
    "list_query",
    "list_sends_folder",
    "scope_sends_folders",
    "list_check",
    "scope_check",
    "scoped_cast_to",
    "check_folders_arg",
    "streamed_error",
    "raise_if_route_not_offered",
    "session_check",
    "session_fallback_check",
]


def is_top_level(folder: str) -> bool:
    """Whether `folder` names the top level: only spaces (U+0020) and `/`, or empty.

    These are exactly the characters the API strips from both ends of a path.
    Any other value, a tab or a no-break space included, is sent as given.
    """
    return folder.strip(" /") == ""


def _given(value: object) -> bool:
    return value is not None and not isinstance(value, (Omit, NotGiven))


def list_query(file_ids: object, folder: object, recursive: object) -> Dict[str, object]:
    """The query of `sources.list`.

    A top-level `folder` is sent as `recursive=false` with no `folder`: an empty
    query value is not sent at all, so `folder=""` would otherwise list every
    source.
    """
    if isinstance(folder, str) and is_top_level(folder):
        return {"file_ids": file_ids, "recursive": False}
    return {"file_ids": file_ids, "folder": folder, "recursive": recursive}


def list_sends_folder(folder: object, recursive: object) -> bool:
    return isinstance(folder, str) or isinstance(recursive, bool)


def scope_sends_folders(folders: object) -> bool:
    if not _given(folders) or isinstance(folders, str):
        return False
    try:
        return len(cast(Any, folders)) > 0
    except TypeError:
        return False


def check_folders_arg(folders: object) -> None:
    """Refuse a `folders` that is not a list of paths before any request.

    A string is a sequence too, so `folders="Contracts"` would otherwise be
    sent as given and neither checked nor applied the way it reads.
    """
    if not _given(folders):
        return
    if isinstance(folders, (str, bytes, bytearray)) or not isinstance(folders, Sequence):
        raise GraphorError('`folders` must be a list of folder paths, such as ["Contracts"].')


def _not_applied(parameter: str, *, conversation_id: Optional[str] = None) -> FolderScopeNotAppliedError:
    return FolderScopeNotAppliedError(
        f"The API did not apply the `{parameter}` parameter, so the result was not returned: "
        "it may cover more sources than were asked for. The API may not support folders.",
        parameter=parameter,
        conversation_id=conversation_id,
    )


_UNREADABLE = (httpx.Response, str, bytes, bytearray)
"""Results parsed with `parse(to=...)` into a type the checks cannot read: not checked, as raw bytes."""


def _field(obj: object, key: str) -> object:
    """A field of a parsed model or of a mapping (`parse(to=Dict[...])`)."""
    if isinstance(obj, Mapping):
        return cast(Mapping[str, object], obj).get(key)  # pyright: ignore[reportUnknownMemberType]
    return getattr(obj, key, None)


def list_check(folder: object) -> Callable[[Any], Any]:
    """A `post_parser` for `sources.list`: every source must carry `folder`."""
    parameter = "folder" if isinstance(folder, str) else "recursive"

    def check(parsed: Any) -> Any:
        if isinstance(parsed, _UNREADABLE):
            return parsed
        if parsed is None:
            return parsed
        if not isinstance(parsed, list):
            raise _not_applied(parameter)
        for source in cast(List[object], parsed):
            if not isinstance(_field(source, "folder"), str):
                raise _not_applied(parameter)
        return cast(Any, parsed)

    return check


def _envelope(data: object) -> Optional[Dict[str, object]]:
    """A failure streamed after the answer started: `status_code` (an int) and `detail`."""
    status = _field(data, "status_code")
    if isinstance(status, int) and not isinstance(status, bool) and _field(data, "detail") is not None:
        return _body_of(data)
    return None


def scope_check(client: Any, method: str, path: str) -> Callable[[Any], Any]:
    """A `post_parser` for `ask`, `extract` and `retrieve_chunks` sent with `folders`.

    A long answer streams whitespace first, so a failure after that arrives as
    a 200 body with `status_code` and `detail`; it raises the status error that
    status would raise. Otherwise the answer must echo `folders`.
    """

    def check(parsed: Any) -> Any:
        if isinstance(parsed, _UNREADABLE):
            return parsed
        envelope = _envelope(parsed)
        if envelope is not None:
            raise streamed_error(client, method, path, envelope)
        if not _field(parsed, "folders"):
            conversation_id = _field(parsed, "conversation_id")
            raise _not_applied("folders", conversation_id=conversation_id if isinstance(conversation_id, str) else None)
        return parsed

    return check


_strict_builders: Dict[type, type] = {}


def scoped_cast_to(client: Any, model: Type[_M]) -> Type[_M]:
    """The `cast_to` of a scoped `ask` or `extract`.

    With strict response validation, a streamed failure would fail validation
    before the check could read it, so it is built without validation and
    raised by `scope_check`; any other body is validated as usual.
    """
    if not getattr(client, "_strict_response_validation", False):
        return model
    builder = _strict_builders.get(model)
    if builder is None:

        def build(cls: type, *, response: httpx.Response, data: object) -> object:  # noqa: ARG001
            if _envelope(data) is not None:
                return construct_type(type_=model, value=data)
            return validate_type(type_=model, value=data)

        builder = cast(type, type(model.__name__, (model,), {"build": classmethod(build)}))
        _strict_builders[model] = builder
    return cast(Type[_M], builder)


def _body_of(parsed: Any) -> Dict[str, object]:
    if isinstance(parsed, Mapping):
        return dict(cast(Mapping[str, object], parsed))
    to_dict = getattr(parsed, "to_dict", None)
    if callable(to_dict):
        return cast(Dict[str, object], to_dict())
    return {}


def streamed_error(client: Any, method: str, path: str, body: Dict[str, object]) -> Exception:
    status = body.get("status_code")
    status = status if isinstance(status, int) and not isinstance(status, bool) and status >= 400 else 500
    headers: Dict[str, str] = {}
    retry_after = body.get("retry_after")
    if isinstance(retry_after, (int, float)) and not isinstance(retry_after, bool):
        headers["retry-after"] = str(retry_after)
    request = httpx.Request(method, client._prepare_url(path))
    response = httpx.Response(status, request=request, headers=headers, json=body)
    return cast(Exception, client._make_status_error(str(body.get("detail")), body=body, response=response))


def _is_mapping(value: object) -> bool:
    return isinstance(value, Mapping)


def _has_code(body: object) -> bool:
    """Whether an error body carries a non-empty string `code`."""
    code = _field(body, "code") if _is_mapping(body) else None
    return isinstance(code, str) and code != ""


def raise_if_route_not_offered(error: NotFoundError, route: str) -> None:
    """A 404 without a `code` means the API does not offer the folder route.

    It raises `FolderScopeNotAppliedError` with `parameter` set to the route
    (for example `POST /sources/rename-folder`), so it is never read as
    "already done". A 404 with a `code` (`folder.not_found`) is the API's
    answer: this returns, and the caller raises the error as it is.
    """
    if _has_code(error.body):
        return
    raise FolderScopeNotAppliedError(
        f"The API does not offer `{route}`. The API may not support folders.",
        parameter=route,
    ) from error


def session_fallback_check(folder: object, error: Exception) -> None:
    """A large upload with `folder` never falls back after the framework's own 404.

    An API without upload sessions does not support folders either, and the
    direct request would store the file at the top level.
    """
    if (
        isinstance(folder, str)
        and isinstance(error, NotFoundError)
        and _is_mapping(error.body)
        and not _has_code(error.body)
    ):
        raise _not_applied("folder") from error


def session_check(folder: object, session_folder: object) -> None:
    """An upload session created with `folder` must echo it (`""` is the top level)."""
    if isinstance(folder, str) and not isinstance(session_folder, str):
        raise _not_applied("folder")
