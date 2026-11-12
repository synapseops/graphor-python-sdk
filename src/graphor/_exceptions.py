# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

__all__ = [
    "UploadError",
    "FolderScopeNotAppliedError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
]


class GraphorError(Exception):
    pass


class APIError(GraphorError):
    message: str
    request: httpx.Request

    body: object | None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:  # noqa: ARG002
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body


class APIResponseValidationError(APIError):
    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, body: object | None, *, message: str | None = None) -> None:
        super().__init__(message or "Data returned by API invalid for expected schema.", response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    def __init__(self, message: str, *, response: httpx.Response, body: object | None) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIConnectionError(APIError):
    def __init__(self, *, message: str = "Connection error.", request: httpx.Request) -> None:
        super().__init__(message, request, body=None)


class UploadError(APIError):
    """Raised when the bytes of a large file could not be uploaded or completed.

    `offset` is how many bytes the upload had stored when it stopped (`-1` when
    the bytes were all sent and completing them failed). `build_id` is set when
    the upload may still finish: check that build before uploading again.
    """

    offset: int
    status_code: int | None
    build_id: str | None

    def __init__(
        self,
        message: str,
        *,
        request: httpx.Request,
        offset: int,
        status_code: int | None = None,
        build_id: str | None = None,
    ) -> None:
        super().__init__(message, request, body=None)
        self.offset = offset
        self.status_code = status_code
        self.build_id = build_id


class FolderScopeNotAppliedError(GraphorError):
    """Raised when the API did not apply a folder parameter, so the SDK refused the result.

    The API says which folder filter or scope it applied: `folder` on every
    listed source, `folders` on `ask`, `extract` and `retrieve_chunks`, and
    `folder` on an upload session. When a call sent one of these and the answer
    does not carry it, the API ignored it (it does not support folders), and the
    result could cover more than was asked for, so it is not returned. The same
    error is raised when the API does not offer a folder route.

    `parameter` names what was not applied (`folder`, `recursive` or `folders`),
    or the route the API does not offer (for example `POST /sources/rename-folder`).
    `conversation_id` is set for `ask`: the API already answered and recorded that
    turn in the conversation, so repeat the question with `reset=True` or in a new
    conversation. This error is never retried.
    """

    message: str
    parameter: str
    conversation_id: str | None

    def __init__(self, message: str, *, parameter: str, conversation_id: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.parameter = parameter
        self.conversation_id = conversation_id


class APITimeoutError(APIConnectionError):
    def __init__(self, request: httpx.Request) -> None:
        super().__init__(message="Request timed out.", request=request)


class BadRequestError(APIStatusError):
    status_code: Literal[400] = 400  # pyright: ignore[reportIncompatibleVariableOverride]


class AuthenticationError(APIStatusError):
    status_code: Literal[401] = 401  # pyright: ignore[reportIncompatibleVariableOverride]


class PermissionDeniedError(APIStatusError):
    status_code: Literal[403] = 403  # pyright: ignore[reportIncompatibleVariableOverride]


class NotFoundError(APIStatusError):
    status_code: Literal[404] = 404  # pyright: ignore[reportIncompatibleVariableOverride]


class ConflictError(APIStatusError):
    status_code: Literal[409] = 409  # pyright: ignore[reportIncompatibleVariableOverride]


class UnprocessableEntityError(APIStatusError):
    status_code: Literal[422] = 422  # pyright: ignore[reportIncompatibleVariableOverride]


class RateLimitError(APIStatusError):
    status_code: Literal[429] = 429  # pyright: ignore[reportIncompatibleVariableOverride]


class InternalServerError(APIStatusError):
    pass
