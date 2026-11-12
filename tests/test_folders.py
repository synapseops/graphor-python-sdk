"""Folders: what the folder methods and parameters send, and the checks that the
API applied them, against a fake API."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Callable, Optional, cast

import httpx
import pytest

from graphor import (
    Graphor,
    AsyncGraphor,
    GraphorError,
    NotFoundError,
    APIStatusError,
    BadRequestError,
    InternalServerError,
    APIResponseValidationError,
    FolderScopeNotAppliedError,
)
from graphor.types import SourceAskResponse
from graphor._folders import is_top_level
from graphor._response import APIResponse

BASE_URL = "https://api.example.test/v1"

SOURCE: Dict[str, Any] = {
    "file_id": "f1",
    "file_name": "a.pdf",
    "file_size": 10,
    "file_source": "local_file",
    "file_type": "pdf",
    "message": "Source processed successfully",
    "project_id": "p1",
    "project_name": "Project",
    "status": "completed",
}
FRAMEWORK_404 = {"detail": "Not Found"}


class FakeAPI:
    """Records each request and answers with the next scripted response, or a default."""

    def __init__(self) -> None:
        self.requests: List[httpx.Request] = []
        self.script: List[Callable[[httpx.Request], httpx.Response]] = []
        self.default: Callable[[httpx.Request], httpx.Response] = lambda _r: httpx.Response(200, json={})

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if self.script:
            return self.script.pop(0)(request)
        return self.default(request)

    def answer(self, status: int, body: Any, headers: Optional[Dict[str, str]] = None) -> None:
        self.default = lambda _r: httpx.Response(status, json=body, headers=headers)

    def last(self) -> httpx.Request:
        return self.requests[-1]

    def last_json(self) -> Dict[str, Any]:
        return json.loads(self.last().content)

    def last_query(self) -> List[tuple[str, str]]:
        return list(self.last().url.params.multi_items())


@pytest.fixture
def api() -> FakeAPI:
    return FakeAPI()


def _client(api: FakeAPI, **kwargs: Any) -> Graphor:
    return Graphor(
        api_key="test-key",
        base_url=BASE_URL,
        http_client=httpx.Client(transport=httpx.MockTransport(api.handler)),
        **kwargs,
    )


def _async_client(api: FakeAPI, **kwargs: Any) -> AsyncGraphor:
    return AsyncGraphor(
        api_key="test-key",
        base_url=BASE_URL,
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(api.handler)),
        **kwargs,
    )


# --- the top-level test -------------------------------------------------------


@pytest.mark.parametrize("value", ["", "/", " ", "//", " / ", "  ///  "])
def test_top_level_spellings(value: str) -> None:
    assert is_top_level(value)


@pytest.mark.parametrize("value", ["a", "/a/", "\t", "\n", " ", "　", " \t/"])
def test_other_values_are_not_the_top_level(value: str) -> None:
    assert not is_top_level(value)


# --- list: the query -----------------------------------------------------------


def test_list_without_folder_parameters_sends_none(api: FakeAPI) -> None:
    api.answer(200, [SOURCE])
    result = _client(api).sources.list()
    assert api.last_query() == []
    assert result[0].folder is None  # an answer without `folder` is fine when no filter was sent


def test_list_sends_a_path_and_recursive(api: FakeAPI) -> None:
    api.answer(200, [{**SOURCE, "folder": "X"}])
    _client(api).sources.list(folder="X", recursive=False)
    assert api.last_query() == [("folder", "X"), ("recursive", "false")]


def test_list_sends_a_folder_with_a_comma_as_one_value(api: FakeAPI) -> None:
    api.answer(200, [])
    _client(api).sources.list(folder="Smith, Jones/2026")
    assert api.last_query() == [("folder", "Smith, Jones/2026")]


@pytest.mark.parametrize("value", ["", "/", " ", "//", " / "])
@pytest.mark.parametrize("recursive", [None, True, False])
def test_list_sends_the_top_level_as_recursive_false(api: FakeAPI, value: str, recursive: Optional[bool]) -> None:
    api.answer(200, [])
    if recursive is None:
        _client(api).sources.list(folder=value)
    else:
        _client(api).sources.list(folder=value, recursive=recursive)
    assert api.last_query() == [("recursive", "false")]


@pytest.mark.parametrize("value", ["\t", "\n", " ", "　"])
def test_list_sends_other_blanks_as_given(api: FakeAPI, value: str) -> None:
    api.answer(200, [])
    _client(api).sources.list(folder=value)
    assert api.last_query() == [("folder", value)]


def test_list_keeps_file_ids(api: FakeAPI) -> None:
    api.answer(200, [])
    _client(api).sources.list(file_ids=["a", "b"], folder="/")
    assert api.last_query() == [("file_ids", "a,b"), ("recursive", "false")]


# --- list: the check -------------------------------------------------------------


@pytest.mark.parametrize(
    "kwargs", [{"folder": "X"}, {"folder": "/"}, {"folder": ""}, {"recursive": True}, {"recursive": False}]
)
def test_list_without_folder_on_a_source_raises(api: FakeAPI, kwargs: Dict[str, Any]) -> None:
    api.answer(200, [{**SOURCE, "folder": ""}, SOURCE])
    with pytest.raises(FolderScopeNotAppliedError) as info:
        _client(api).sources.list(**kwargs)
    assert info.value.parameter == ("folder" if "folder" in kwargs else "recursive")


def test_list_with_folder_on_every_source_passes(api: FakeAPI) -> None:
    api.answer(200, [{**SOURCE, "folder": ""}, {**SOURCE, "folder": "X/Y"}])
    result = _client(api).sources.list(folder="X")
    assert [s.folder for s in result] == ["", "X/Y"]


def test_an_empty_list_passes(api: FakeAPI) -> None:
    api.answer(200, [])
    assert _client(api).sources.list(folder="X") == []


def test_list_raw_wrapper_returns_a_response_and_parse_raises(api: FakeAPI) -> None:
    api.answer(200, [SOURCE])
    raw = _client(api).sources.with_raw_response.list(folder="X")
    assert isinstance(raw, APIResponse)
    with pytest.raises(FolderScopeNotAppliedError):
        raw.parse()
    assert json.loads(raw.text()) == [SOURCE]  # the raw bytes are not checked


def test_list_streaming_wrapper_parse_raises(api: FakeAPI) -> None:
    api.answer(200, [SOURCE])
    with _client(api).sources.with_streaming_response.list(folder="X") as response:
        with pytest.raises(FolderScopeNotAppliedError):
            response.parse()


async def test_async_list_checks_and_maps_the_top_level(api: FakeAPI) -> None:
    api.answer(200, [SOURCE])
    client = _async_client(api)
    with pytest.raises(FolderScopeNotAppliedError):
        await client.sources.list(folder="/")
    assert api.last_query() == [("recursive", "false")]
    raw = await client.sources.with_raw_response.list(recursive=True)
    with pytest.raises(FolderScopeNotAppliedError):
        await raw.parse()


# --- ask, extract, retrieve -----------------------------------------------------

SCOPED: List[Any] = [
    ("ask", {"question": "q"}, "/sources/ask-sources", {"answer": "a", "conversation_id": "c1"}),
    ("extract", {"output_schema": {}, "user_instruction": "u"}, "/sources/run-extraction", {"file_names": []}),
    ("retrieve_chunks", {"query": "q"}, "/sources/prebuilt-rag", {"query": "q", "total": 0}),
]
LATE_503 = {
    "detail": "The service is busy. Try again shortly.",
    "code": "service.unavailable",
    "reference": "ref-1",
    "status_code": 503,
    "retryable": True,
    "retry_after": 30,
    "busy": False,
}


@pytest.mark.parametrize(("method", "args", "path", "answer"), SCOPED)
def test_scope_sends_folders_and_passes_with_the_echo(
    api: FakeAPI, method: str, args: Dict[str, Any], path: str, answer: Dict[str, Any]
) -> None:
    api.answer(200, {**answer, "folders": ["Contracts"]})
    result = getattr(_client(api).sources, method)(**args, folders=[" /Contracts/ "])
    assert api.last().url.path.endswith(path)
    assert api.last_json()["folders"] == [" /Contracts/ "]
    assert result.folders == ["Contracts"]


@pytest.mark.parametrize(("method", "args", "path", "answer"), SCOPED)
@pytest.mark.parametrize("folders", ["omitted", None, []])
def test_scope_without_folders_is_not_checked(
    api: FakeAPI, method: str, args: Dict[str, Any], path: str, answer: Dict[str, Any], folders: Any
) -> None:
    api.answer(200, answer)
    kwargs = {} if folders == "omitted" else {"folders": folders}
    getattr(_client(api).sources, method)(**args, **kwargs)
    assert api.last().url.path.endswith(path)
    body = api.last_json()
    if folders == "omitted":
        assert "folders" not in body
    else:
        assert body["folders"] == folders


@pytest.mark.parametrize(("method", "args", "path", "answer"), SCOPED)
@pytest.mark.parametrize("echo", ["missing", None, []])
def test_scope_without_the_echo_raises(
    api: FakeAPI, method: str, args: Dict[str, Any], path: str, answer: Dict[str, Any], echo: Any
) -> None:
    del path
    api.answer(200, answer if echo == "missing" else {**answer, "folders": echo})
    with pytest.raises(FolderScopeNotAppliedError) as info:
        getattr(_client(api).sources, method)(**args, folders=["Contracts"])
    assert info.value.parameter == "folders"


def test_a_withheld_ask_carries_its_conversation(api: FakeAPI) -> None:
    api.answer(200, {"answer": "a", "conversation_id": "c1"})
    with pytest.raises(FolderScopeNotAppliedError) as info:
        _client(api).sources.ask(question="q", folders=["Contracts"])
    assert info.value.conversation_id == "c1"


@pytest.mark.parametrize(("method", "args", "path", "answer"), SCOPED)
def test_a_streamed_failure_raises_its_status_error(
    api: FakeAPI, method: str, args: Dict[str, Any], path: str, answer: Dict[str, Any]
) -> None:
    del answer
    api.default = lambda _r: httpx.Response(200, content=b"   \n " + json.dumps(LATE_503).encode())
    with pytest.raises(InternalServerError) as info:
        getattr(_client(api).sources, method)(**args, folders=["Contracts"])
    error = info.value
    assert error.status_code == 503
    body = cast(Dict[str, Any], error.body)
    assert body["code"] == "service.unavailable"
    assert body["retry_after"] == 30 and body["reference"] == "ref-1" and body["status_code"] == 503
    assert error.response.headers["retry-after"] == "30"
    assert str(error.request.url).endswith(path)


def test_a_streamed_400_raises_bad_request(api: FakeAPI) -> None:
    api.answer(200, {"detail": "No", "code": "request.invalid", "status_code": 400, "retryable": False})
    with pytest.raises(BadRequestError):
        _client(api).sources.extract(output_schema={}, user_instruction="u", folders=["X"])


def test_an_error_body_without_status_is_not_applied(api: FakeAPI) -> None:
    # An API without folders streams `detail` and `code` only.
    api.answer(200, {"detail": "Failed", "code": "internal"})
    with pytest.raises(FolderScopeNotAppliedError):
        _client(api).sources.ask(question="q", folders=["X"])


def test_ask_raw_and_streaming_parse_are_checked(api: FakeAPI) -> None:
    api.answer(200, LATE_503)
    client = _client(api)
    raw = client.sources.with_raw_response.ask(question="q", folders=["X"])
    assert isinstance(raw, APIResponse)
    with pytest.raises(InternalServerError):
        raw.parse()
    with client.sources.with_streaming_response.ask(question="q", folders=["X"]) as response:
        with pytest.raises(InternalServerError):
            response.parse()
    api.answer(200, {"answer": "a"})
    with pytest.raises(FolderScopeNotAppliedError):
        client.sources.with_raw_response.retrieve_chunks(query="q", folders=["X"]).parse()


async def test_async_scope_checks(api: FakeAPI) -> None:
    client = _async_client(api)
    api.answer(200, LATE_503)
    with pytest.raises(InternalServerError) as info:
        await client.sources.ask(question="q", folders=["X"])
    assert info.value.status_code == 503
    raw = await client.sources.with_raw_response.extract(output_schema={}, user_instruction="u", folders=["X"])
    with pytest.raises(InternalServerError):
        await raw.parse()
    api.answer(200, {"query": "q", "total": 0})
    with pytest.raises(FolderScopeNotAppliedError):
        await client.sources.retrieve_chunks(query="q", folders=["X"])
    api.answer(200, {"query": "q", "total": 0, "folders": ["X"]})
    assert (await client.sources.retrieve_chunks(query="q", folders=["X"])).folders == ["X"]


def test_strict_validation_still_refuses_a_missing_echo(api: FakeAPI) -> None:
    api.answer(200, {"answer": "a"})
    with pytest.raises(FolderScopeNotAppliedError):
        _client(api, _strict_response_validation=True).sources.ask(question="q", folders=["X"])


# --- the folder methods -----------------------------------------------------------

FOLDER_CALLS: List[Any] = [
    ("list_folders", {}, "GET", "/sources/folders", None, {"folders": [{"folder": "A"}], "truncated": False}),
    (
        "create_folder",
        {"folder": "A"},
        "POST",
        "/sources/create-folder",
        {"folder": "A"},
        {"folder": "A", "created": True},
    ),
    (
        "rename_folder",
        {"folder": "A", "new_folder": "B"},
        "POST",
        "/sources/rename-folder",
        {"folder": "A", "new_folder": "B"},
        {"folder": "A", "new_folder": "B", "moved": 1},
    ),
    (
        "remove_folder",
        {"folder": "A/B", "merge": True},
        "POST",
        "/sources/remove-folder",
        {"folder": "A/B", "merge": True},
        {"folder": "A/B", "parent": "A", "moved": 2},
    ),
    (
        "delete_folder",
        {"folder": "A"},
        "POST",
        "/sources/delete-folder",
        {"folder": "A"},
        {"folder": "A", "deleted": 1},
    ),
    (
        "move",
        {"file_ids": ["f1", "f2"], "folder": ""},
        "POST",
        "/sources/move-sources",
        {"file_ids": ["f1", "f2"], "folder": ""},
        {"folder": "", "moved": 1, "not_found": ["f2"]},
    ),
]
NAMES = [call[0] for call in FOLDER_CALLS]


@pytest.mark.parametrize(("name", "args", "verb", "path", "body", "answer"), FOLDER_CALLS)
def test_folder_methods_send_and_parse(
    api: FakeAPI, name: str, args: Dict[str, Any], verb: str, path: str, body: Any, answer: Dict[str, Any]
) -> None:
    api.answer(200, answer)
    result = getattr(_client(api).sources, name)(**args)
    request = api.last()
    assert request.method == verb and request.url.path == "/v1" + path
    if body is not None:
        assert api.last_json() == body
    assert result.to_dict() == answer


@pytest.mark.parametrize(("name", "args", "verb", "path", "body", "answer"), FOLDER_CALLS)
def test_a_framework_404_means_the_route_is_not_offered(
    api: FakeAPI, name: str, args: Dict[str, Any], verb: str, path: str, body: Any, answer: Any
) -> None:
    del body, answer
    api.answer(404, FRAMEWORK_404)
    client = _client(api)
    with pytest.raises(FolderScopeNotAppliedError) as info:
        getattr(client.sources, name)(**args)
    assert info.value.parameter == f"{verb} {path}"
    assert isinstance(info.value.__cause__, NotFoundError)
    with pytest.raises(FolderScopeNotAppliedError):
        getattr(client.sources.with_raw_response, name)(**args)
    with pytest.raises(FolderScopeNotAppliedError):
        with getattr(client.sources.with_streaming_response, name)(**args):
            pass


@pytest.mark.parametrize(("name", "args", "verb", "path", "body", "answer"), FOLDER_CALLS)
async def test_async_framework_404(
    api: FakeAPI, name: str, args: Dict[str, Any], verb: str, path: str, body: Any, answer: Any
) -> None:
    del verb, path, body, answer
    api.answer(404, FRAMEWORK_404)
    client = _async_client(api)
    with pytest.raises(FolderScopeNotAppliedError):
        await getattr(client.sources, name)(**args)
    with pytest.raises(FolderScopeNotAppliedError):
        await getattr(client.sources.with_raw_response, name)(**args)
    with pytest.raises(FolderScopeNotAppliedError):
        async with getattr(client.sources.with_streaming_response, name)(**args):
            pass


@pytest.mark.parametrize("name", ["rename_folder", "remove_folder", "delete_folder"])
def test_a_coded_404_is_the_apis_answer(api: FakeAPI, name: str) -> None:
    api.answer(404, {"detail": "The folder was not found.", "code": "folder.not_found"})
    args = {"folder": "A", "new_folder": "B"} if name == "rename_folder" else {"folder": "A"}
    with pytest.raises(NotFoundError) as info:
        getattr(_client(api).sources, name)(**args)
    assert not isinstance(info.value, FolderScopeNotAppliedError)


def test_merge_is_sent_only_when_given(api: FakeAPI) -> None:
    api.answer(200, {"folder": "A", "new_folder": "B", "moved": 0})
    _client(api).sources.rename_folder(folder="A", new_folder="B")
    assert api.last_json() == {"folder": "A", "new_folder": "B"}
    _client(api).sources.rename_folder(folder="A", new_folder="B", merge=False)
    assert api.last_json() == {"folder": "A", "new_folder": "B", "merge": False}


# --- retries ----------------------------------------------------------------------

UNSAFE: List[Any] = [
    ("rename_folder", {"folder": "A", "new_folder": "B"}),
    ("remove_folder", {"folder": "A"}),
    ("delete_folder", {"folder": "A"}),
]
BUSY = {"detail": "Busy", "code": "service.unavailable"}


@pytest.mark.parametrize(("name", "args"), UNSAFE)
def test_unsafe_methods_never_retry_a_503(api: FakeAPI, name: str, args: Dict[str, Any]) -> None:
    api.answer(503, BUSY, headers={"x-should-retry": "true", "retry-after": "0"})
    for client in (_client(api, max_retries=3), _client(api).with_options(max_retries=5)):
        api.requests.clear()
        with pytest.raises(InternalServerError):
            getattr(client.sources, name)(**args)
        assert len(api.requests) == 1


@pytest.mark.parametrize(("name", "args"), UNSAFE)
def test_unsafe_methods_never_retry_a_timeout(api: FakeAPI, name: str, args: Dict[str, Any]) -> None:
    def timeout(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("timed out", request=request)

    api.default = timeout
    with pytest.raises(Exception):  # noqa: B017
        getattr(_client(api, max_retries=3).sources, name)(**args)
    assert len(api.requests) == 1


@pytest.mark.parametrize(("name", "args"), UNSAFE)
async def test_async_unsafe_methods_never_retry(api: FakeAPI, name: str, args: Dict[str, Any]) -> None:
    api.answer(503, BUSY, headers={"x-should-retry": "true", "retry-after": "0"})
    with pytest.raises(InternalServerError):
        await getattr(_async_client(api, max_retries=3).sources, name)(**args)
    assert len(api.requests) == 1


@pytest.mark.parametrize(
    ("name", "args"), [("create_folder", {"folder": "A"}), ("move", {"file_ids": ["f1"], "folder": "A"})]
)
def test_safe_methods_keep_the_clients_retries(api: FakeAPI, name: str, args: Dict[str, Any]) -> None:
    api.answer(503, BUSY, headers={"x-should-retry": "true", "retry-after": "0"})
    with pytest.raises(InternalServerError):
        getattr(_client(api, max_retries=2).sources, name)(**args)
    assert len(api.requests) == 3


# --- the wrappers -------------------------------------------------------------------


def test_every_folder_method_is_on_each_wrapper(api: FakeAPI) -> None:
    client, async_client = _client(api), _async_client(api)
    for resource in (
        client.sources,
        client.sources.with_raw_response,
        client.sources.with_streaming_response,
        async_client.sources,
        async_client.sources.with_raw_response,
        async_client.sources.with_streaming_response,
    ):
        for name in NAMES:
            assert callable(getattr(resource, name)), (type(resource).__name__, name)


# --- uploads and links ----------------------------------------------------------------


def _form_fields(request: httpx.Request) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    content = request.content.decode("latin-1")
    for part in content.split("Content-Disposition: form-data; ")[1:]:
        header, _, value = part.partition("\r\n\r\n")
        name = header.split('name="', 1)[1].split('"', 1)[0]
        fields[name] = value.rsplit("\r\n--", 1)[0]
    return fields


def test_ingest_file_sends_folder_in_the_form(api: FakeAPI) -> None:
    api.answer(200, {"build_id": "b1"})
    client = _client(api)
    client.sources.ingest_file(file=("a.pdf", b"%PDF"), folder="Contracts/2026")
    assert _form_fields(api.last())["folder"] == "Contracts/2026"
    client.sources.ingest_file(file=("a.pdf", b"%PDF"))
    assert "folder" not in _form_fields(api.last())


@pytest.mark.parametrize("method", ["ingest_url", "ingest_github", "ingest_youtube"])
def test_links_send_folder_as_given(api: FakeAPI, method: str) -> None:
    api.answer(200, {"build_id": "b1"})
    call = getattr(_client(api).sources, method)
    call(url="https://example.com/x")
    assert "folder" not in api.last_json()
    for value in (None, "", "/", "A/B"):
        call(url="https://example.com/x", folder=value)
        assert api.last_json()["folder"] == value


def test_a_status_error_is_not_folder_scope_not_applied() -> None:
    # The large-upload fallback catches status errors; this one must never be one.
    assert not issubclass(FolderScopeNotAppliedError, APIStatusError)


# --- parse(to=...) ------------------------------------------------------------------


def test_scope_check_reads_a_dict_parse(api: FakeAPI) -> None:
    client = _client(api)
    api.answer(200, {"answer": "a", "folders": ["A"]})
    parsed = client.sources.with_raw_response.ask(question="q", folders=["A"]).parse(to=Dict[str, Any])
    assert parsed == {"answer": "a", "folders": ["A"]}
    api.answer(200, {"answer": "a", "conversation_id": "c1"})
    with pytest.raises(FolderScopeNotAppliedError) as info:
        client.sources.with_raw_response.ask(question="q", folders=["A"]).parse(to=Dict[str, Any])
    assert info.value.conversation_id == "c1"
    api.answer(200, LATE_503)
    with pytest.raises(InternalServerError) as error:
        client.sources.with_raw_response.extract(output_schema={}, user_instruction="u", folders=["A"]).parse(
            to=Dict[str, object]
        )
    assert error.value.status_code == 503


def test_list_check_reads_a_list_of_dicts(api: FakeAPI) -> None:
    client = _client(api)
    api.answer(200, [{**SOURCE, "folder": "A"}])
    parsed = client.sources.with_raw_response.list(folder="A").parse(to=List[Dict[str, Any]])
    assert parsed[0]["folder"] == "A"
    api.answer(200, [SOURCE])
    with pytest.raises(FolderScopeNotAppliedError):
        client.sources.with_raw_response.list(folder="A").parse(to=List[Dict[str, Any]])


def test_a_parse_to_raw_types_is_not_checked(api: FakeAPI) -> None:
    client = _client(api)
    api.answer(200, [SOURCE])
    raw = client.sources.with_raw_response.list(folder="A")
    assert isinstance(raw.parse(to=httpx.Response), httpx.Response)
    assert json.loads(raw.parse(to=str)) == [SOURCE]
    api.answer(200, {"answer": "a"})
    raw_ask = client.sources.with_raw_response.ask(question="q", folders=["A"])
    assert isinstance(raw_ask.parse(to=httpx.Response), httpx.Response)


# --- strict response validation --------------------------------------------------------


def test_strict_mode_raises_a_streamed_failure_as_its_status(api: FakeAPI) -> None:
    client = _client(api, _strict_response_validation=True)
    api.answer(200, LATE_503)
    with pytest.raises(InternalServerError) as info:
        client.sources.ask(question="q", folders=["A"])
    assert info.value.status_code == 503
    with pytest.raises(InternalServerError):
        client.sources.extract(output_schema={}, user_instruction="u", folders=["A"])
    with pytest.raises(InternalServerError):
        client.sources.with_raw_response.ask(question="q", folders=["A"]).parse()
    with client.sources.with_streaming_response.extract(
        output_schema={}, user_instruction="u", folders=["A"]
    ) as response:
        with pytest.raises(InternalServerError):
            response.parse()


def test_strict_mode_still_validates_a_scoped_answer(api: FakeAPI) -> None:
    client = _client(api, _strict_response_validation=True)
    api.answer(200, {"answer": "a", "folders": ["A"]})
    result = client.sources.ask(question="q", folders=["A"])
    assert type(result) is SourceAskResponse and result.folders == ["A"]
    api.answer(200, {"folders": ["A"]})  # no `answer`
    with pytest.raises(APIResponseValidationError):
        client.sources.ask(question="q", folders=["A"])


async def test_async_strict_mode_raises_a_streamed_failure_as_its_status(api: FakeAPI) -> None:
    client = _async_client(api, _strict_response_validation=True)
    api.answer(200, LATE_503)
    with pytest.raises(InternalServerError):
        await client.sources.ask(question="q", folders=["A"])
    raw = await client.sources.with_raw_response.extract(output_schema={}, user_instruction="u", folders=["A"])
    with pytest.raises(InternalServerError):
        await raw.parse()


# --- the route parameter ------------------------------------------------------------


@pytest.mark.parametrize("body", [FRAMEWORK_404, {"detail": "Not Found", "code": ""}, {"detail": "x", "code": None}])
def test_a_404_without_a_string_code_is_a_missing_route(api: FakeAPI, body: Dict[str, Any]) -> None:
    api.answer(404, body)
    with pytest.raises(FolderScopeNotAppliedError) as info:
        _client(api).sources.delete_folder(folder="A")
    assert info.value.parameter == "POST /sources/delete-folder"


# --- a `folders` that is not a list ---------------------------------------------------


@pytest.mark.parametrize(("method", "args", "path", "answer"), SCOPED)
@pytest.mark.parametrize("folders", ["Contracts", b"Contracts", {"Contracts"}, 3])
def test_folders_that_is_not_a_list_is_refused_before_any_request(
    api: FakeAPI, method: str, args: Dict[str, Any], path: str, answer: Dict[str, Any], folders: Any
) -> None:
    del path, answer
    with pytest.raises(GraphorError) as info:
        getattr(_client(api).sources, method)(**args, folders=folders)
    assert not isinstance(info.value, FolderScopeNotAppliedError)
    assert "must be a list of folder paths" in str(info.value)
    assert api.requests == []


async def test_async_folders_that_is_not_a_list_is_refused(api: FakeAPI) -> None:
    with pytest.raises(GraphorError):
        await _async_client(api).sources.ask(question="q", folders=cast(Any, "Contracts"))
    assert api.requests == []


def test_a_tuple_of_folders_is_sent(api: FakeAPI) -> None:
    api.answer(200, {"query": "q", "total": 0, "folders": ["A"]})
    _client(api).sources.retrieve_chunks(query="q", folders=("A",))
    assert api.last_json()["folders"] == ["A"]
