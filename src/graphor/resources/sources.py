# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    Method,
    source_ask_params,
    source_list_params,
    source_move_params,
    source_delete_params,
    source_extract_params,
    source_reprocess_params,
    source_ingest_url_params,
    source_index_build_params,
    source_ingest_file_params,
    source_get_elements_params,
    source_create_folder_params,
    source_delete_folder_params,
    source_ingest_github_params,
    source_remove_folder_params,
    source_rename_folder_params,
    source_ingest_youtube_params,
    source_retrieve_chunks_params,
    source_get_build_status_params,
    source_get_page_screenshot_params,
)
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._folders import (
    list_check,
    list_query,
    scope_check,
    scoped_cast_to,
    check_folders_arg,
    list_sends_folder,
    scope_sends_folders,
    raise_if_route_not_offered,
)
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._exceptions import NotFoundError
from .._base_client import make_request_options
from ..types.method import Method
from .._large_upload import rewind, upload, async_upload, prepare_upload, async_prepare_upload
from ..types.source_ask_response import SourceAskResponse
from ..types.source_list_response import SourceListResponse
from ..types.source_move_response import SourceMoveResponse
from ..types.source_delete_response import SourceDeleteResponse
from ..types.source_extract_response import SourceExtractResponse
from ..types.source_reprocess_response import SourceReprocessResponse
from ..types.source_ingest_url_response import SourceIngestURLResponse
from ..types.source_index_build_response import SourceIndexBuildResponse
from ..types.source_ingest_file_response import SourceIngestFileResponse
from ..types.source_get_elements_response import SourceGetElementsResponse
from ..types.source_list_folders_response import SourceListFoldersResponse
from ..types.source_create_folder_response import SourceCreateFolderResponse
from ..types.source_delete_folder_response import SourceDeleteFolderResponse
from ..types.source_ingest_github_response import SourceIngestGitHubResponse
from ..types.source_remove_folder_response import SourceRemoveFolderResponse
from ..types.source_rename_folder_response import SourceRenameFolderResponse
from ..types.source_ingest_youtube_response import SourceIngestYoutubeResponse
from ..types.source_retrieve_chunks_response import SourceRetrieveChunksResponse
from ..types.source_get_build_status_response import SourceGetBuildStatusResponse
from ..types.source_get_page_screenshot_response import SourceGetPageScreenshotResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/synapseops/graphor-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/synapseops/graphor-python-sdk#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        folder: str | Omit = omit,
        recursive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """
        List all sources in the project's knowledge graph.

        Returns every source node currently stored in the knowledge graph for the
        authenticated project. Each item includes the file metadata (ID, name, size,
        type, origin) along with its current processing status and a human-readable
        status message.

        **Query parameters:**

        - **file_ids** (list, optional): If provided, only sources whose file_id is in
          this list are returned. Repeat the param for multiple IDs (e.g.
          ?file_ids=id1&file_ids=id2).
        - **folder** (str, optional): Only the sources in this folder and, with
          `recursive=True` (the default), below it. An empty string or `/` lists only
          the top level.
        - **recursive** (bool, optional, default `True`): With `folder`, whether the
          folders below it are included. Without `folder`, `False` lists only the top
          level.

        Every source carries `folder`, its folder's path (`""` at the top level).

        **Status messages returned per source:**

        - `"completed"` → _"Source processed successfully"_
        - `"processing"` → _"Source is being processed"_
        - `"failed"` → _"Source processing failed"_

        **Returns** a JSON array of `PublicSourceResponse` objects.

        **Error responses:**

        - `422` — Invalid folder.
        - `500` — Unexpected internal error while retrieving sources.

        Args:
          file_ids: Optional list of file_id to filter by (only these sources are returned). Repeat
              the param for multiple IDs.

          folder: Only the sources in this folder, a '/'-separated path, and (with
              `recursive`, the default) in the folders below it. An empty string or '/' (any
              value made only of spaces and slashes) lists only the top level; it is sent as
              `recursive=false`. An invalid path answers 422.

          recursive: With `folder`, include the folders below it (default `True`). Without
              `folder`, `False` lists only the sources at the top level.

              When `folder` or `recursive` is given, every returned source must carry
              `folder`; if one does not, the API did not apply the filter and
              `FolderScopeNotAppliedError` is raised instead of returning the list. The
              check runs when the result is parsed, also through `.with_raw_response` and
              `.with_streaming_response` (`.parse()`), but not on the raw bytes, nor on a
              `.parse(to=...)` into `httpx.Response`, `str` or `bytes`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(list_query(file_ids, folder, recursive), source_list_params.SourceListParams),
                post_parser=list_check(folder) if list_sends_folder(folder, recursive) else not_given,
            ),
            cast_to=SourceListResponse,
        )

    def delete(
        self,
        *,
        file_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteResponse:
        """
        Delete a source from the project's knowledge graph and all associated data.

        Removes the source node, its partitions/chunks, embeddings, and any stored files
        from the knowledge graph and object storage. The operation is irreversible.

        **Parameters (JSON body):**

        - **file_id** (str, optional — preferred): The unique identifier of the source
          to delete.
        - **file_name** (str, optional — deprecated): The display name of the source.
          Use `file_id` instead when possible. At least one of `file_id` or `file_name`
          must be provided.

        **Returns** a `PublicDeleteSourceResponse` with the deletion status, file ID,
        file name, project ID, and project name.

        **Error responses:**

        - `400` — Invalid input (e.g. neither identifier provided).
        - `403` — Permission denied.
        - `404` — Source not found.
        - `500` — Unexpected internal error.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file to delete (deprecated, use file_id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/sources/delete",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                },
                source_delete_params.SourceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceDeleteResponse,
        )

    def ask(
        self,
        *,
        question: str,
        conversation_id: Optional[str] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
        folders: Optional[SequenceNotStr[str]] | Omit = omit,
        include_citation_images: Optional[bool] | Omit = omit,
        include_citation_markup: Optional[bool] | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reset: Optional[bool] | Omit = omit,
        thinking_level: Optional[Literal["fast", "balanced", "accurate", "max"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceAskResponse:
        """
        Ask a natural-language question grounded on the project's ingested sources.

        This is the primary Q&A endpoint. It sends the question through native RAG
        retrieval (legacy builds indexed with Google File Search still use that engine),
        which retrieves relevant chunks from the knowledge graph, grounds the answer in
        the source documents, and returns a natural-language response. Optionally, you
        can request a structured JSON output by supplying an `output_schema`.

        Conversation memory is supported: pass a `conversation_id` to continue an
        existing conversation, or set `reset` to `true` to start fresh.

        **Parameters (JSON body):**

        - **question** (str, required): The question to ask about the sources.
        - **conversation_id** (str, optional): An existing conversation identifier to
          maintain context across multiple turns.
        - **reset** (bool, optional, default `false`): When `true`, starts a new
          conversation discarding any previous history.
        - **file_ids** (list[str], optional — preferred): Restrict the search scope to
          specific source file IDs.
        - **file_names** (list[str], optional — deprecated): Restrict the search scope
          to specific source file names. Use `file_ids` when possible.
        - **folders** (list[str], optional): Restrict the scope to every source at or
          below each folder, together with `file_ids`. An empty list is no folder scope.
        - **output_schema** (dict, optional): A JSON Schema for requesting structured
          output. When provided, the response includes a `structured_output` field
          validated against this schema and the `raw_json` produced by the model.
        - **thinking_level** (str, optional, default `"accurate"`): Controls the
          model/thinking budget — one of `"fast"`, `"balanced"`, or `"accurate"`.

        **Returns** a `PublicAskSourcesResponse` containing:

        - `answer` — the natural-language answer (or a status message when
          `output_schema` is provided).
        - `structured_output` — the validated structured object (when `output_schema` is
          provided).
        - `raw_json` — the raw JSON text before validation (when `output_schema` is
          provided).
        - `conversation_id` — the conversation identifier for follow-up questions.

        **Error responses:**

        - `500` — Unexpected internal error while asking sources.

        Args:
          question: The natural-language question to ask about the sources

          conversation_id: Conversation identifier to maintain memory context across multiple turns

          file_ids: Optional list of file IDs to restrict search scope (preferred)

          file_names: Optional list of file display names to restrict search scope (deprecated, use
              file_ids)

          folders: Folders to restrict the scope to (at most 1,000): every source at or below
              each folder, read when the request arrives, together with any `file_ids`. An
              empty list is no folder scope. A folder that holds no source answers 400
              `chat.folder_scope_empty`; the top level, an invalid path, or `folders` with
              `file_names` answers 422. When `folders` is not empty and the answer does not
              echo it, the API did not apply it and `FolderScopeNotAppliedError` is raised
              instead of returning the result; a failure streamed after the answer started
              raises the error for its status. Both checks run when the result is parsed,
              also through `.with_raw_response` and `.with_streaming_response` (`.parse()`),
              but not on the raw bytes (`.http_response`, `.read()`, `.text()`, `.json()`)
              nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A `folders`
              that is not a list (a string, for example) is refused before any request.

          include_citation_images: When true, the response's `citations` entries are populated with a
              base64-encoded PNG screenshot of each cited page in `image_base64`. Increases
              payload size and latency — leave false (the default) when not needed and fetch
              screenshots on demand via
              `GET /sources/{file_id}/pages/{page_number}/screenshot`.

          include_citation_markup: When true, the `answer` field keeps the structured citation markup
              `[N](file_id|pX|sY|eZ|fNAME)` emitted by the agent. When false (default), the
              markup is stripped to plain `[N]` markers and the structured data is exposed via
              `citations` instead. Note: the markup format is an implementation detail and may
              change in future versions — prefer the `citations` field for stable parsing. Has
              no effect when `output_schema` is set.

          output_schema: Optional JSON Schema for requesting structured output. When provided, the answer
              field will contain a short status message and the structured data will be in
              structured_output.

          reset: When true, starts a new conversation discarding any previous history

          thinking_level: Controls model and thinking budget: 'fast' (premium output speed), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        check_folders_arg(folders)
        return self._post(
            "/sources/ask-sources",
            body=maybe_transform(
                {
                    "question": question,
                    "conversation_id": conversation_id,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "folders": folders,
                    "include_citation_images": include_citation_images,
                    "include_citation_markup": include_citation_markup,
                    "output_schema": output_schema,
                    "reset": reset,
                    "thinking_level": thinking_level,
                },
                source_ask_params.SourceAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=scope_check(self._client, "POST", "/sources/ask-sources")
                if scope_sends_folders(folders)
                else not_given,
            ),
            cast_to=scoped_cast_to(self._client, SourceAskResponse)
            if scope_sends_folders(folders)
            else SourceAskResponse,
        )

    def extract(
        self,
        *,
        output_schema: Dict[str, object],
        user_instruction: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
        folders: Optional[SequenceNotStr[str]] | Omit = omit,
        thinking_level: Optional[Literal["fast", "balanced", "accurate", "max"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceExtractResponse:
        """
        Run a one-off structured data extraction against one or more sources.

        This endpoint uses native RAG retrieval (legacy builds indexed with Google File
        Search still use that engine) to read the specified sources, apply the
        user-provided instruction, and return structured JSON output conforming to the
        supplied `output_schema`. Internally it builds a grounded prompt, queries the
        model, and validates/corrects the raw JSON against the schema.

        **Parameters (JSON body):**

        - **file_ids** (list[str], optional — preferred): List of source file IDs to
          extract from.
        - **file_names** (list[str], optional — deprecated): List of source file names
          to extract from. Use `file_ids` when possible.
        - **folders** (list[str], optional): Folders to extract from: every source at
          or below each folder, together with `file_ids`. At least one of `file_ids`,
          `file_names` or `folders` must be provided and non-empty.
        - **user_instruction** (str, required): A natural-language instruction that
          guides what information to extract from the documents.
        - **output_schema** (dict, required): A JSON Schema object describing the
          desired structured output shape. The model will produce data conforming to
          this schema.
        - **thinking_level** (str, optional, default `"accurate"`): Controls the
          model/thinking budget — one of `"fast"`, `"balanced"`, or `"accurate"`.

        **Returns** a `PublicRunExtractionResultResponse` containing:

        - `structured_output` — the validated structured object.
        - `raw_json` — the raw JSON text produced by the model before validation.

        **Error responses:**

        - `500` — Unexpected internal error during extraction.

        Args:
          output_schema: JSON Schema describing the desired structured output shape. The model will
              produce data conforming to this schema.

          user_instruction: Natural-language instruction guiding what information to extract

          file_ids: List of file IDs to extract from (preferred)

          file_names: List of file names to extract from (deprecated, use file_ids)

          folders: Folders to restrict the scope to (at most 1,000): every source at or below
              each folder, read when the request arrives, together with any `file_ids`. An
              empty list is no folder scope. A folder that holds no source answers 400
              `chat.folder_scope_empty`; the top level, an invalid path, or `folders` with
              `file_names` answers 422. When `folders` is not empty and the answer does not
              echo it, the API did not apply it and `FolderScopeNotAppliedError` is raised
              instead of returning the result; a failure streamed after the answer started
              raises the error for its status. Both checks run when the result is parsed,
              also through `.with_raw_response` and `.with_streaming_response` (`.parse()`),
              but not on the raw bytes (`.http_response`, `.read()`, `.text()`, `.json()`)
              nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A `folders`
              that is not a list (a string, for example) is refused before any request.

          thinking_level: Controls model and thinking budget: 'fast' (premium output speed), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        check_folders_arg(folders)
        return self._post(
            "/sources/run-extraction",
            body=maybe_transform(
                {
                    "output_schema": output_schema,
                    "user_instruction": user_instruction,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "folders": folders,
                    "thinking_level": thinking_level,
                },
                source_extract_params.SourceExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=scope_check(self._client, "POST", "/sources/run-extraction")
                if scope_sends_folders(folders)
                else not_given,
            ),
            cast_to=scoped_cast_to(self._client, SourceExtractResponse)
            if scope_sends_folders(folders)
            else SourceExtractResponse,
        )

    def get_build_status(
        self,
        build_id: str,
        *,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        suppress_elements: bool | Omit = omit,
        suppress_img_base64: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetBuildStatusResponse:
        """
        Return the status and optional parsed elements for an async build identified by
        `build_id`.

        Use this endpoint to poll the result of an async ingestion or re-process
        request. The `build_id` is returned in the response of:

        - `POST /v2/sources/upload` (async file upload)
        - `POST /v2/sources/upload-url-source` (async URL ingestion)
        - `POST /v2/sources/upload-github-source` (async GitHub ingestion)
        - `POST /v2/sources/upload-youtube-source` (async YouTube ingestion)
        - `POST /v2/sources/process` (async re-process)

        **Path parameter:**

        - **build_id** (str, required): The build identifier returned when the job was
          scheduled.

        **Query parameters:**

        - **suppress_elements** (bool, default `false`): When `true`, elements are
          omitted from the response. When `false` (default), the response includes the
          parsed elements (chunks/partitions) for the build if it completed
          successfully. Same structure as `POST /sources/elements` (each element has
          `page_content` and `metadata`). If `page` and `page_size` are not passed, all
          elements are returned.
        - **suppress_img_base64** (bool, default `false`): When `true`, `img_base64` is
          omitted from each element (useful to reduce payload size when images are not
          needed).
        - **page** (int, optional): 1-based page number. Only used when
          `suppress_elements=false` and pagination is used (pass either `page` or
          `page_size` to enable pagination).
        - **page_size** (int, optional): Number of elements per page (max 100). Only
          used when `suppress_elements=false` and pagination is used.

        **Response fields:**

        - **build_id**: The requested build identifier.
        - **status**: SourceNodeStatus value when history exists (e.g. Processed,
          Processing, Processing failed). `not_found` when no history exists (build in
          progress or invalid id).
        - **success**: `true` when the build completed (status is "Completed" or
          "Completed with errors").
        - **file_id**, **file_name**: Source identifiers; present when the build has
          been persisted (history exists).
        - **error**: Error message from the pipeline when the build failed.
        - **method**, **total_partitions**, **total_pages**: Build metadata when history
          exists.
        - **created_at**, **updated_at**: ISO8601 timestamps when history exists.
        - **document_annotation**: Document-level summary/annotation from the build
          history when available.
        - **message**: Human-readable message (e.g. when status is `not_found`).
        - **elements**: List of `{ page_content, metadata }` when
          `suppress_elements=false` and the build completed successfully.
        - **total_elements**, **page**, **page_size**, **total_pages_elements**:
          Pagination metadata for `elements` when `suppress_elements=false`.

        **Error responses:**

        - `500` — Unexpected internal error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not build_id:
            raise ValueError(f"Expected a non-empty value for `build_id` but received {build_id!r}")
        return self._get(
            path_template("/sources/builds/{build_id}", build_id=build_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "suppress_elements": suppress_elements,
                        "suppress_img_base64": suppress_img_base64,
                    },
                    source_get_build_status_params.SourceGetBuildStatusParams,
                ),
            ),
            cast_to=SourceGetBuildStatusResponse,
        )

    def get_elements(
        self,
        *,
        file_id: str,
        element_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        elements_to_remove: Optional[SequenceNotStr[str]] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_numbers: Optional[Iterable[int]] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        suppress_img_base64: bool | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetElementsResponse:
        """
        Retrieve the parsed elements (chunks/partitions) of a source in the same format
        as get_build_status.

        Returns elements with explicit fields: element_id, element_type, text, markdown,
        html, img_base64 (optional), position, page_number, bounding_box, page_layout,
        etc.

        **Query parameters:**

        - **file_id** (str, required): Unique identifier of the source.
        - **page** (int, optional): 1-based page number. Use with page_size to enable
          pagination.
        - **page_size** (int, optional): Number of elements per page (max 100).
        - **suppress_img_base64** (bool, default false): When true, img_base64 is
          omitted from each element.
        - **type** (str, optional): Filter by element type (e.g. NarrativeText, Title,
          Table).
        - **page_numbers** (list, optional): Restrict to specific page numbers (repeat
          param for multiple).
        - **element_ids** (list, optional): Restrict to specific partition element_ids
          (repeat param for multiple).
        - **elementsToRemove** (list, optional): Element types to exclude (repeat param
          for multiple).

        **Returns** Paginated response with items as BuildStatusElement list (same shape
        as GET /builds/{build_id} elements).

        Args:
          file_id: Unique identifier of the source

          element_ids: Restrict to specific element IDs (repeat param for multiple)

          elements_to_remove: Element types to exclude

          page: 1-based page number (use with page_size)

          page_numbers: Restrict to specific page numbers

          page_size: Number of elements per page

          suppress_img_base64: When true, img_base64 is omitted from each element

          type: Filter by element type (e.g. NarrativeText, Title)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sources/get-elements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_id": file_id,
                        "element_ids": element_ids,
                        "elements_to_remove": elements_to_remove,
                        "page": page,
                        "page_numbers": page_numbers,
                        "page_size": page_size,
                        "suppress_img_base64": suppress_img_base64,
                        "type": type,
                    },
                    source_get_elements_params.SourceGetElementsParams,
                ),
            ),
            cast_to=SourceGetElementsResponse,
        )

    def get_page_screenshot(
        self,
        page_number: int,
        *,
        file_id: str,
        max_width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetPageScreenshotResponse:
        """
        Render a single page of a source file as a base64-encoded PNG screenshot.

        Use this endpoint to lazily fetch the visual preview of a citation returned by
        `/ask-sources` without paying the payload cost of inlining base64 in the answer.
        Supports PDFs, image files (`page_number` must be 1), and Office documents
        (doc/docx/ppt/pptx/odt — rendered from the converted PDF).

        **Path parameters:**

        - **file_id** (str): UUID of the source file.
        - **page_number** (int): 1-based page number.

        **Query parameters:**

        - **max_width** (int, optional, default `900`): Pixel width cap. Clamped to the
          300-1600 range.

        **Returns** a `PublicPageScreenshotResponse` containing:

        - `file_id`, `file_name`, `page_number` — identifying metadata.
        - `mime_type` — always `"image/png"`.
        - `width`, `height` — rendered image dimensions in pixels.
        - `image_base64` — the base64-encoded PNG bytes.

        **Error responses:**

        - `404` — File not found, unsupported file type, or invalid page number.
        - `500` — Unexpected internal error while rendering.

        Args:
          max_width: Pixel width cap for the rendered image (clamped to 300-1600).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template(
                "/sources/{file_id}/pages/{page_number}/screenshot", file_id=file_id, page_number=page_number
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"max_width": max_width}, source_get_page_screenshot_params.SourceGetPageScreenshotParams
                ),
            ),
            cast_to=SourceGetPageScreenshotResponse,
        )

    def index_build(
        self,
        *,
        file_id: str,
        build_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIndexBuildResponse:
        """
        Build the retrieval index for an existing build from its already-parsed
        partitions — the way out of `indexing=none` without paying for a re-parse.

        Chunks, embeds and indexes the build's persisted partitions, makes it the file's
        active build, and flips the persisted `indexing` level to `full`. After it
        returns, `ask-sources`, `run-extraction` and `prebuilt-rag` see the source, and
        build status reports `searchable: true`.

        **Parameters (JSON body):**

        - **file_id** (str, required): Unique identifier of the source file.
        - **build_id** (str, optional): Build to index. Omitted → the file's active
          build. A non-active build becomes active (only the active build can serve
          retrieval).

        Synchronous: the response arrives when indexing finishes. For large documents
        the connection is kept alive with whitespace heartbeats — JSON parsers ignore
        them, no client change needed.

        **Returns** `PublicIndexBuildResponse` with `chunks_indexed`.

        Args:
          file_id: Unique identifier of the source file.

          build_id: Build to index. Omitted → the file's active build. When given, that build
              becomes the active one (only the active build can serve retrieval).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/index",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "build_id": build_id,
                },
                source_index_build_params.SourceIndexBuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIndexBuildResponse,
        )

    def ingest_file(
        self,
        *,
        file: FileTypes,
        enrichment: Optional[str] | Omit = omit,
        folder: str | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        method: Optional[Method] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestFileResponse:
        """
        Upload a local file and schedule ingestion in the background.

        Validates the file's size and extension, stores it, then schedules the full
        data-ingestion pipeline in the background. Returns with a `build_id` to poll
        for status. Files above the direct upload limit (30 MiB) are sent in chunks
        that resume after a network error, which can take a while for a large file;
        `timeout` then applies to each request, not to the whole upload.

        **Parameters:**

        - **file** (`multipart/form-data`): The file to upload. Must include
          `Content-Length` and have a supported extension (pdf, doc, docx, csv, txt, md,
          etc.).
        - **method** (`form`, optional): Partitioning strategy. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`, `auto`. Default when omitted.
        - **enrichment** (`form`, optional): `full` (default) or `none`. `none` skips
          LLM page/section/document annotation for faster, cheaper parsing.
        - **indexing** (`form`, optional): `full` (default) or `none`. `none` skips
          chunking/embedding/indexing — the source is parsed but not searchable via
          ask/extract/retrieve. Check `GET /v2/sources/config` for availability.
        - **folder** (`form`, optional): The folder to store the source in; empty, `/`
          or omitted is the top level.

        **Returns** `AsyncIngestResponse` with `build_id`. Use it to check processing
        status.

        Args:
          enrichment: LLM enrichment level: 'full' (default) or 'none' to skip page/section/document
              annotation for faster parsing.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); empty, '/' or omitted is the top level. A folder that does
              not exist is created. An invalid path answers 400. For a file sent through an
              upload session the folder is fixed when the session starts, and the upload
              stops with `FolderScopeNotAppliedError`, before any byte is sent, if the API
              does not confirm it, or if the API offers no upload sessions (then it does not
              support folders either).

          indexing: Retrieval indexing level: 'full' (default) or 'none' to skip
              chunking/embedding/indexing — the source is parsed but not searchable. Requires
              Temporal ingestion.

          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm
              - auto → auto

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        file, large = prepare_upload(file)

        def direct() -> SourceIngestFileResponse:
            rewind(file)
            body = deepcopy_with_paths(
                {
                    "file": file,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                    "method": method,
                },
                [["file"]],
            )
            files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
            return self._post(
                "/sources/ingest-file",
                body=maybe_transform(body, source_ingest_file_params.SourceIngestFileParams),
                files=files,
                options=make_request_options(
                    extra_headers=headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceIngestFileResponse,
            )

        if large is None:
            return direct()
        # Above the direct upload limit: an upload session (see `_large_upload`).
        return cast(
            SourceIngestFileResponse,
            upload(
                self,
                large,
                direct=direct,
                method=method,
                enrichment=enrichment,
                indexing=indexing,
                folder=folder,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def ingest_github(
        self,
        *,
        url: str,
        enrichment: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestGitHubResponse:
        """
        Ingest a GitHub repository as a source into the project's knowledge graph.

        Schedules the ingestion in the background and returns immediately with a
        `build_id`. Use the returned `build_id` to poll for processing status.

        **Parameters (JSON body):**

        - **url** (str, required): The GitHub repository URL to ingest (e.g.
          `https://github.com/owner/repo`).

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          url: The GitHub repository URL to ingest (e.g. https://github.com/owner/repo)

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); an empty string or '/' is the top level. A folder that does
              not exist is created. When omitted, a new source goes to the top level and a
              source that replaces one of the same name keeps that source's folder.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/ingest-github",
            body=maybe_transform(
                {
                    "url": url,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                },
                source_ingest_github_params.SourceIngestGitHubParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestGitHubResponse,
        )

    def ingest_url(
        self,
        *,
        url: str,
        crawl_urls: bool | Omit = omit,
        enrichment: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        method: Optional[Method] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestURLResponse:
        """
        Ingest a web page (or a set of crawled pages) as a source into the project's
        knowledge graph.

        Unlike the synchronous version, this endpoint schedules the ingestion in the
        background and returns immediately with a `processing` status. The source will
        be fully available once background processing completes.

        If the URL points directly to a downloadable file (detected via URL path
        extension or HTTP Content-Type), the file is first downloaded and uploaded to
        storage synchronously, then the partition/embedding pipeline runs in the
        background.

        **Parameters (JSON body):**

        - **url** (str, required): The web page URL to ingest.
        - **crawlUrls** (bool, optional, default `false`): When `true`, the system will
          also follow and ingest links found on the page. Ignored when the URL resolves
          to a file.
        - **method** (str, optional): The partitioning strategy to use. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`, `auto`. When omitted the system
          default is applied.

        **Returns** a `PublicSourceResponse` with `status: "processing"` immediately.
        Poll the source status endpoint using the returned `file_id` to track
        completion.

        **Error responses:**

        - `400` — Unsupported file type detected from a file URL.
        - `500` — Unexpected internal error during URL processing.

        Args:
          url: The web page URL to ingest

          crawl_urls: When true, also follows and ingests links found on the page

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); an empty string or '/' is the top level. A folder that does
              not exist is created. When omitted, a new source goes to the top level and a
              source that replaces one of the same name keeps that source's folder.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm
              - auto → auto

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/ingest-url",
            body=maybe_transform(
                {
                    "url": url,
                    "crawl_urls": crawl_urls,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                    "method": method,
                },
                source_ingest_url_params.SourceIngestURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestURLResponse,
        )

    def ingest_youtube(
        self,
        *,
        url: str,
        enrichment: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestYoutubeResponse:
        """
        Ingest a YouTube video as a source into the project's knowledge graph.

        Schedules the ingestion in the background and returns immediately with a
        `build_id`. The endpoint will download the transcript/captions and process them
        in the background. Use the returned `build_id` to poll for processing status.

        **Parameters (JSON body):**

        - **url** (str, required): The YouTube video URL to ingest (e.g.
          `https://www.youtube.com/watch?v=...`).

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          url: The YouTube video URL to ingest (e.g.
              https://www.youtube.com/watch?v=dQw4w9WgXcQ)

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); an empty string or '/' is the top level. A folder that does
              not exist is created. When omitted, a new source goes to the top level and a
              source that replaces one of the same name keeps that source's folder.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/ingest-youtube",
            body=maybe_transform(
                {
                    "url": url,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                },
                source_ingest_youtube_params.SourceIngestYoutubeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestYoutubeResponse,
        )

    def reprocess(
        self,
        *,
        file_id: str,
        enrichment: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        method: Method | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceReprocessResponse:
        """
        Re-process (re-parse) an existing source in the background.

        Schedules the data-ingestion pipeline (partitioning, chunking, embedding) for an
        existing source and returns immediately with a `build_id`. Use it to poll for
        status.

        **Parameters (JSON body):**

        - **file_id** (str, required): Unique identifier of the source to re-process.
        - **method** (str, default `"fast"`): Partitioning strategy. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`, `auto`.

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          file_id: Unique identifier of the source to re-process.

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          method: Partitioning strategy. One of: fast, balanced, accurate, agentic, auto.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/reprocess",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "enrichment": enrichment,
                    "indexing": indexing,
                    "method": method,
                },
                source_reprocess_params.SourceReprocessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceReprocessResponse,
        )

    def retrieve_chunks(
        self,
        *,
        query: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
        folders: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRetrieveChunksResponse:
        """
        Retrieve relevant document chunks from the prebuilt RAG vector store.

        Performs a semantic similarity search over the project's prebuilt RAG store
        using Google File Search with grounding. Returns the most relevant text chunks
        along with their source metadata (file name, page number, relevance score). This
        is a pure retrieval endpoint — it does **not** generate an answer; use
        `/ask-sources` for Q&A.

        **Parameters (JSON body):**

        - **query** (str, required): The natural-language search query used to find
          relevant chunks.
        - **file_ids** (list[str], optional — preferred): Restrict retrieval to specific
          source file IDs.
        - **file_names** (list[str], optional — deprecated): Restrict retrieval to
          specific source file names. Use `file_ids` when possible.
        - **folders** (list[str], optional): Restrict the scope to every source at or
          below each folder, together with `file_ids`. An empty list is no folder scope.

        **Returns** a `PublicRetrieveResponse` containing:

        - `query` — the original search query.
        - `chunks` — a list of `PublicRetrieveChunk` objects, each with `text`,
          `file_name`, `page_number`, `score`, and additional `metadata`.
        - `total` — the total number of chunks returned.

        **Error responses:**

        - `500` — Unexpected internal error during retrieval.

        Args:
          query: The natural-language search query to find relevant chunks

          file_ids: Optional list of file IDs to restrict retrieval scope (preferred)

          file_names: Optional list of file names to restrict retrieval scope (deprecated, use
              file_ids)

          folders: Folders to restrict the scope to (at most 1,000): every source at or below
              each folder, read when the request arrives, together with any `file_ids`. An
              empty list is no folder scope. A folder that holds no source answers 400
              `chat.folder_scope_empty`; the top level, an invalid path, or `folders` with
              `file_names` answers 422. When `folders` is not empty and the answer does not
              echo it, the API did not apply it and `FolderScopeNotAppliedError` is raised
              instead of returning the result; a failure streamed after the answer started
              raises the error for its status. Both checks run when the result is parsed,
              also through `.with_raw_response` and `.with_streaming_response` (`.parse()`),
              but not on the raw bytes (`.http_response`, `.read()`, `.text()`, `.json()`)
              nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A `folders`
              that is not a list (a string, for example) is refused before any request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        check_folders_arg(folders)
        return self._post(
            "/sources/prebuilt-rag",
            body=maybe_transform(
                {
                    "query": query,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "folders": folders,
                },
                source_retrieve_chunks_params.SourceRetrieveChunksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=scope_check(self._client, "POST", "/sources/prebuilt-rag")
                if scope_sends_folders(folders)
                else not_given,
            ),
            cast_to=SourceRetrieveChunksResponse,
        )

    def list_folders(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListFoldersResponse:
        """
        List every folder of the project, sorted, each with the folders above it.

        Lists folders created empty, folders that hold sources and folders uploads
        are on their way to. At most 10,000 folders are returned, in sort order;
        `truncated` is true when the project has more.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        try:
            return self._get(
                "/sources/folders",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceListFoldersResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "GET /sources/folders")
            raise

    def create_folder(
        self,
        *,
        folder: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceCreateFolderResponse:
        """
        Create a folder that stays listed while it is empty, with the folders above it.

        Safe to repeat: `created` is false when the folder existed. An upload or a
        move into a folder that does not exist creates it, so this is needed only for
        an empty folder.

        **Error responses:**

        - `409` — `folder.too_many`: the project holds the most folders it can.
        - `422` — Invalid path, or the top level.
        - `503` — The folder could not be saved; retry.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder's path, '/'-separated (for example `Contracts/2026`). Not the
              top level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        try:
            return self._post(
                "/sources/create-folder",
                body=maybe_transform({"folder": folder}, source_create_folder_params.SourceCreateFolderParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceCreateFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/create-folder")
            raise

    def rename_folder(
        self,
        *,
        folder: str,
        new_folder: str,
        merge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRenameFolderResponse:
        """
        Rename a folder, or move it under another folder, with everything in it.

        **Not safe to repeat blindly.** After a 503, a timeout or a lost answer the
        change may have been saved, and a repeat can answer 404 `folder.not_found`
        although the first call worked. So this method never retries on its own,
        whatever `max_retries` says on the client or in `with_options`: call
        `list_folders()` and repeat by hand only if the change is not there. Only a
        404 whose `code` is `folder.not_found` may mean an earlier call worked.

        **Error responses:**

        - `400` — `folder.into_itself` (a folder into its own subfolder) or
          `folder.path_too_long` (a moved path breaks the path rules).
        - `404` — `folder.not_found`.
        - `409` — `folder.exists`: `new_folder` exists and `merge` is not set.
        - `422` — Invalid path, or the top level.
        - `503` — The change may or may not have been saved; list the folders before
          repeating.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder to rename

          new_folder: Its new path; it may sit under another folder

          merge: Merge into `new_folder` when it already exists, instead of answering 409
              `folder.exists`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        options["max_retries"] = 0  # never repeated on its own: see above
        try:
            return self._post(
                "/sources/rename-folder",
                body=maybe_transform(
                    {
                        "folder": folder,
                        "new_folder": new_folder,
                        "merge": merge,
                    },
                    source_rename_folder_params.SourceRenameFolderParams,
                ),
                options=options,
                cast_to=SourceRenameFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/rename-folder")
            raise

    def remove_folder(
        self,
        *,
        folder: str,
        merge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRemoveFolderResponse:
        """
        Remove a folder and move its sources and subfolders into the folder above it
        (the top level for a top-level folder).

        **Not safe to repeat blindly.** After a 503, a timeout or a lost answer the
        change may have been saved, and a repeat can answer 404 `folder.not_found`
        although the first call worked. So this method never retries on its own,
        whatever `max_retries` says on the client or in `with_options`: call
        `list_folders()` and repeat by hand only if the change is not there. Only a
        404 whose `code` is `folder.not_found` may mean an earlier call worked.

        **Error responses:**

        - `404` — `folder.not_found`.
        - `409` — `folder.exists`: a subfolder has the name of a folder above and
          `merge` is not set.
        - `422` — Invalid path, or the top level.
        - `503` — The change may or may not have been saved; list the folders before
          repeating.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder to remove

          merge: Merge a subfolder into a folder of the same name above it, instead of
              answering 409 `folder.exists`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        options["max_retries"] = 0  # never repeated on its own: see above
        try:
            return self._post(
                "/sources/remove-folder",
                body=maybe_transform(
                    {
                        "folder": folder,
                        "merge": merge,
                    },
                    source_remove_folder_params.SourceRemoveFolderParams,
                ),
                options=options,
                cast_to=SourceRemoveFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/remove-folder")
            raise

    def delete_folder(
        self,
        *,
        folder: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteFolderResponse:
        """
        Delete an empty folder and the empty folders below it.

        Its sources must be moved (`move`) or deleted first.

        **Not safe to repeat blindly.** After a 503, a timeout or a lost answer the
        change may have been saved, and a repeat can answer 404 `folder.not_found`
        although the first call worked. So this method never retries on its own,
        whatever `max_retries` says on the client or in `with_options`: call
        `list_folders()` and repeat by hand only if the change is not there. Only a
        404 whose `code` is `folder.not_found` may mean an earlier call worked.

        **Error responses:**

        - `404` — `folder.not_found`.
        - `409` — `folder.not_empty` (it holds a source) or `folder.uploads_pending`
          (uploads into it are not stored yet).
        - `422` — Invalid path, or the top level.
        - `503` — The change may or may not have been saved; list the folders before
          repeating.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        options["max_retries"] = 0  # never repeated on its own: see above
        try:
            return self._post(
                "/sources/delete-folder",
                body=maybe_transform({"folder": folder}, source_delete_folder_params.SourceDeleteFolderParams),
                options=options,
                cast_to=SourceDeleteFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/delete-folder")
            raise

    def move(
        self,
        *,
        file_ids: SequenceNotStr[str],
        folder: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceMoveResponse:
        """
        Move up to 1,000 sources to a folder.

        `""` or `/` is the top level. A folder that does not exist is created. Ids
        that match no source of the project come back in `not_found`. Safe to
        repeat.

        **Error responses:**

        - `409` — `folder.too_many`: the project holds the most folders it can.
        - `422` — Invalid path, or no ids or more than 1,000.
        - `503` — The sources could not be moved; retry.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          file_ids: The sources to move (1 to 1,000)

          folder: The target folder, '/'-separated; an empty string or '/' is the top level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        try:
            return self._post(
                "/sources/move-sources",
                body=maybe_transform(
                    {
                        "file_ids": file_ids,
                        "folder": folder,
                    },
                    source_move_params.SourceMoveParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceMoveResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/move-sources")
            raise


class AsyncSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/synapseops/graphor-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/synapseops/graphor-python-sdk#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        folder: str | Omit = omit,
        recursive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """
        List all sources in the project's knowledge graph.

        Returns every source node currently stored in the knowledge graph for the
        authenticated project. Each item includes the file metadata (ID, name, size,
        type, origin) along with its current processing status and a human-readable
        status message.

        **Query parameters:**

        - **file_ids** (list, optional): If provided, only sources whose file_id is in
          this list are returned. Repeat the param for multiple IDs (e.g.
          ?file_ids=id1&file_ids=id2).
        - **folder** (str, optional): Only the sources in this folder and, with
          `recursive=True` (the default), below it. An empty string or `/` lists only
          the top level.
        - **recursive** (bool, optional, default `True`): With `folder`, whether the
          folders below it are included. Without `folder`, `False` lists only the top
          level.

        Every source carries `folder`, its folder's path (`""` at the top level).

        **Status messages returned per source:**

        - `"completed"` → _"Source processed successfully"_
        - `"processing"` → _"Source is being processed"_
        - `"failed"` → _"Source processing failed"_

        **Returns** a JSON array of `PublicSourceResponse` objects.

        **Error responses:**

        - `422` — Invalid folder.
        - `500` — Unexpected internal error while retrieving sources.

        Args:
          file_ids: Optional list of file_id to filter by (only these sources are returned). Repeat
              the param for multiple IDs.

          folder: Only the sources in this folder, a '/'-separated path, and (with
              `recursive`, the default) in the folders below it. An empty string or '/' (any
              value made only of spaces and slashes) lists only the top level; it is sent as
              `recursive=false`. An invalid path answers 422.

          recursive: With `folder`, include the folders below it (default `True`). Without
              `folder`, `False` lists only the sources at the top level.

              When `folder` or `recursive` is given, every returned source must carry
              `folder`; if one does not, the API did not apply the filter and
              `FolderScopeNotAppliedError` is raised instead of returning the list. The
              check runs when the result is parsed, also through `.with_raw_response` and
              `.with_streaming_response` (`.parse()`), but not on the raw bytes, nor on a
              `.parse(to=...)` into `httpx.Response`, `str` or `bytes`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    list_query(file_ids, folder, recursive), source_list_params.SourceListParams
                ),
                post_parser=list_check(folder) if list_sends_folder(folder, recursive) else not_given,
            ),
            cast_to=SourceListResponse,
        )

    async def delete(
        self,
        *,
        file_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteResponse:
        """
        Delete a source from the project's knowledge graph and all associated data.

        Removes the source node, its partitions/chunks, embeddings, and any stored files
        from the knowledge graph and object storage. The operation is irreversible.

        **Parameters (JSON body):**

        - **file_id** (str, optional — preferred): The unique identifier of the source
          to delete.
        - **file_name** (str, optional — deprecated): The display name of the source.
          Use `file_id` instead when possible. At least one of `file_id` or `file_name`
          must be provided.

        **Returns** a `PublicDeleteSourceResponse` with the deletion status, file ID,
        file name, project ID, and project name.

        **Error responses:**

        - `400` — Invalid input (e.g. neither identifier provided).
        - `403` — Permission denied.
        - `404` — Source not found.
        - `500` — Unexpected internal error.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file to delete (deprecated, use file_id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/sources/delete",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                },
                source_delete_params.SourceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceDeleteResponse,
        )

    async def ask(
        self,
        *,
        question: str,
        conversation_id: Optional[str] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
        folders: Optional[SequenceNotStr[str]] | Omit = omit,
        include_citation_images: Optional[bool] | Omit = omit,
        include_citation_markup: Optional[bool] | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reset: Optional[bool] | Omit = omit,
        thinking_level: Optional[Literal["fast", "balanced", "accurate", "max"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceAskResponse:
        """
        Ask a natural-language question grounded on the project's ingested sources.

        This is the primary Q&A endpoint. It sends the question through native RAG
        retrieval (legacy builds indexed with Google File Search still use that engine),
        which retrieves relevant chunks from the knowledge graph, grounds the answer in
        the source documents, and returns a natural-language response. Optionally, you
        can request a structured JSON output by supplying an `output_schema`.

        Conversation memory is supported: pass a `conversation_id` to continue an
        existing conversation, or set `reset` to `true` to start fresh.

        **Parameters (JSON body):**

        - **question** (str, required): The question to ask about the sources.
        - **conversation_id** (str, optional): An existing conversation identifier to
          maintain context across multiple turns.
        - **reset** (bool, optional, default `false`): When `true`, starts a new
          conversation discarding any previous history.
        - **file_ids** (list[str], optional — preferred): Restrict the search scope to
          specific source file IDs.
        - **file_names** (list[str], optional — deprecated): Restrict the search scope
          to specific source file names. Use `file_ids` when possible.
        - **folders** (list[str], optional): Restrict the scope to every source at or
          below each folder, together with `file_ids`. An empty list is no folder scope.
        - **output_schema** (dict, optional): A JSON Schema for requesting structured
          output. When provided, the response includes a `structured_output` field
          validated against this schema and the `raw_json` produced by the model.
        - **thinking_level** (str, optional, default `"accurate"`): Controls the
          model/thinking budget — one of `"fast"`, `"balanced"`, or `"accurate"`.

        **Returns** a `PublicAskSourcesResponse` containing:

        - `answer` — the natural-language answer (or a status message when
          `output_schema` is provided).
        - `structured_output` — the validated structured object (when `output_schema` is
          provided).
        - `raw_json` — the raw JSON text before validation (when `output_schema` is
          provided).
        - `conversation_id` — the conversation identifier for follow-up questions.

        **Error responses:**

        - `500` — Unexpected internal error while asking sources.

        Args:
          question: The natural-language question to ask about the sources

          conversation_id: Conversation identifier to maintain memory context across multiple turns

          file_ids: Optional list of file IDs to restrict search scope (preferred)

          file_names: Optional list of file display names to restrict search scope (deprecated, use
              file_ids)

          folders: Folders to restrict the scope to (at most 1,000): every source at or below
              each folder, read when the request arrives, together with any `file_ids`. An
              empty list is no folder scope. A folder that holds no source answers 400
              `chat.folder_scope_empty`; the top level, an invalid path, or `folders` with
              `file_names` answers 422. When `folders` is not empty and the answer does not
              echo it, the API did not apply it and `FolderScopeNotAppliedError` is raised
              instead of returning the result; a failure streamed after the answer started
              raises the error for its status. Both checks run when the result is parsed,
              also through `.with_raw_response` and `.with_streaming_response` (`.parse()`),
              but not on the raw bytes (`.http_response`, `.read()`, `.text()`, `.json()`)
              nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A `folders`
              that is not a list (a string, for example) is refused before any request.

          include_citation_images: When true, the response's `citations` entries are populated with a
              base64-encoded PNG screenshot of each cited page in `image_base64`. Increases
              payload size and latency — leave false (the default) when not needed and fetch
              screenshots on demand via
              `GET /sources/{file_id}/pages/{page_number}/screenshot`.

          include_citation_markup: When true, the `answer` field keeps the structured citation markup
              `[N](file_id|pX|sY|eZ|fNAME)` emitted by the agent. When false (default), the
              markup is stripped to plain `[N]` markers and the structured data is exposed via
              `citations` instead. Note: the markup format is an implementation detail and may
              change in future versions — prefer the `citations` field for stable parsing. Has
              no effect when `output_schema` is set.

          output_schema: Optional JSON Schema for requesting structured output. When provided, the answer
              field will contain a short status message and the structured data will be in
              structured_output.

          reset: When true, starts a new conversation discarding any previous history

          thinking_level: Controls model and thinking budget: 'fast' (premium output speed), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        check_folders_arg(folders)
        return await self._post(
            "/sources/ask-sources",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "conversation_id": conversation_id,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "folders": folders,
                    "include_citation_images": include_citation_images,
                    "include_citation_markup": include_citation_markup,
                    "output_schema": output_schema,
                    "reset": reset,
                    "thinking_level": thinking_level,
                },
                source_ask_params.SourceAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=scope_check(self._client, "POST", "/sources/ask-sources")
                if scope_sends_folders(folders)
                else not_given,
            ),
            cast_to=scoped_cast_to(self._client, SourceAskResponse)
            if scope_sends_folders(folders)
            else SourceAskResponse,
        )

    async def extract(
        self,
        *,
        output_schema: Dict[str, object],
        user_instruction: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
        folders: Optional[SequenceNotStr[str]] | Omit = omit,
        thinking_level: Optional[Literal["fast", "balanced", "accurate", "max"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceExtractResponse:
        """
        Run a one-off structured data extraction against one or more sources.

        This endpoint uses native RAG retrieval (legacy builds indexed with Google File
        Search still use that engine) to read the specified sources, apply the
        user-provided instruction, and return structured JSON output conforming to the
        supplied `output_schema`. Internally it builds a grounded prompt, queries the
        model, and validates/corrects the raw JSON against the schema.

        **Parameters (JSON body):**

        - **file_ids** (list[str], optional — preferred): List of source file IDs to
          extract from.
        - **file_names** (list[str], optional — deprecated): List of source file names
          to extract from. Use `file_ids` when possible.
        - **folders** (list[str], optional): Folders to extract from: every source at
          or below each folder, together with `file_ids`. At least one of `file_ids`,
          `file_names` or `folders` must be provided and non-empty.
        - **user_instruction** (str, required): A natural-language instruction that
          guides what information to extract from the documents.
        - **output_schema** (dict, required): A JSON Schema object describing the
          desired structured output shape. The model will produce data conforming to
          this schema.
        - **thinking_level** (str, optional, default `"accurate"`): Controls the
          model/thinking budget — one of `"fast"`, `"balanced"`, or `"accurate"`.

        **Returns** a `PublicRunExtractionResultResponse` containing:

        - `structured_output` — the validated structured object.
        - `raw_json` — the raw JSON text produced by the model before validation.

        **Error responses:**

        - `500` — Unexpected internal error during extraction.

        Args:
          output_schema: JSON Schema describing the desired structured output shape. The model will
              produce data conforming to this schema.

          user_instruction: Natural-language instruction guiding what information to extract

          file_ids: List of file IDs to extract from (preferred)

          file_names: List of file names to extract from (deprecated, use file_ids)

          folders: Folders to restrict the scope to (at most 1,000): every source at or below
              each folder, read when the request arrives, together with any `file_ids`. An
              empty list is no folder scope. A folder that holds no source answers 400
              `chat.folder_scope_empty`; the top level, an invalid path, or `folders` with
              `file_names` answers 422. When `folders` is not empty and the answer does not
              echo it, the API did not apply it and `FolderScopeNotAppliedError` is raised
              instead of returning the result; a failure streamed after the answer started
              raises the error for its status. Both checks run when the result is parsed,
              also through `.with_raw_response` and `.with_streaming_response` (`.parse()`),
              but not on the raw bytes (`.http_response`, `.read()`, `.text()`, `.json()`)
              nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A `folders`
              that is not a list (a string, for example) is refused before any request.

          thinking_level: Controls model and thinking budget: 'fast' (premium output speed), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        check_folders_arg(folders)
        return await self._post(
            "/sources/run-extraction",
            body=await async_maybe_transform(
                {
                    "output_schema": output_schema,
                    "user_instruction": user_instruction,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "folders": folders,
                    "thinking_level": thinking_level,
                },
                source_extract_params.SourceExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=scope_check(self._client, "POST", "/sources/run-extraction")
                if scope_sends_folders(folders)
                else not_given,
            ),
            cast_to=scoped_cast_to(self._client, SourceExtractResponse)
            if scope_sends_folders(folders)
            else SourceExtractResponse,
        )

    async def get_build_status(
        self,
        build_id: str,
        *,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        suppress_elements: bool | Omit = omit,
        suppress_img_base64: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetBuildStatusResponse:
        """
        Return the status and optional parsed elements for an async build identified by
        `build_id`.

        Use this endpoint to poll the result of an async ingestion or re-process
        request. The `build_id` is returned in the response of:

        - `POST /v2/sources/upload` (async file upload)
        - `POST /v2/sources/upload-url-source` (async URL ingestion)
        - `POST /v2/sources/upload-github-source` (async GitHub ingestion)
        - `POST /v2/sources/upload-youtube-source` (async YouTube ingestion)
        - `POST /v2/sources/process` (async re-process)

        **Path parameter:**

        - **build_id** (str, required): The build identifier returned when the job was
          scheduled.

        **Query parameters:**

        - **suppress_elements** (bool, default `false`): When `true`, elements are
          omitted from the response. When `false` (default), the response includes the
          parsed elements (chunks/partitions) for the build if it completed
          successfully. Same structure as `POST /sources/elements` (each element has
          `page_content` and `metadata`). If `page` and `page_size` are not passed, all
          elements are returned.
        - **suppress_img_base64** (bool, default `false`): When `true`, `img_base64` is
          omitted from each element (useful to reduce payload size when images are not
          needed).
        - **page** (int, optional): 1-based page number. Only used when
          `suppress_elements=false` and pagination is used (pass either `page` or
          `page_size` to enable pagination).
        - **page_size** (int, optional): Number of elements per page (max 100). Only
          used when `suppress_elements=false` and pagination is used.

        **Response fields:**

        - **build_id**: The requested build identifier.
        - **status**: SourceNodeStatus value when history exists (e.g. Processed,
          Processing, Processing failed). `not_found` when no history exists (build in
          progress or invalid id).
        - **success**: `true` when the build completed (status is "Completed" or
          "Completed with errors").
        - **file_id**, **file_name**: Source identifiers; present when the build has
          been persisted (history exists).
        - **error**: Error message from the pipeline when the build failed.
        - **method**, **total_partitions**, **total_pages**: Build metadata when history
          exists.
        - **created_at**, **updated_at**: ISO8601 timestamps when history exists.
        - **document_annotation**: Document-level summary/annotation from the build
          history when available.
        - **message**: Human-readable message (e.g. when status is `not_found`).
        - **elements**: List of `{ page_content, metadata }` when
          `suppress_elements=false` and the build completed successfully.
        - **total_elements**, **page**, **page_size**, **total_pages_elements**:
          Pagination metadata for `elements` when `suppress_elements=false`.

        **Error responses:**

        - `500` — Unexpected internal error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not build_id:
            raise ValueError(f"Expected a non-empty value for `build_id` but received {build_id!r}")
        return await self._get(
            path_template("/sources/builds/{build_id}", build_id=build_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "suppress_elements": suppress_elements,
                        "suppress_img_base64": suppress_img_base64,
                    },
                    source_get_build_status_params.SourceGetBuildStatusParams,
                ),
            ),
            cast_to=SourceGetBuildStatusResponse,
        )

    async def get_elements(
        self,
        *,
        file_id: str,
        element_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        elements_to_remove: Optional[SequenceNotStr[str]] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_numbers: Optional[Iterable[int]] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        suppress_img_base64: bool | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetElementsResponse:
        """
        Retrieve the parsed elements (chunks/partitions) of a source in the same format
        as get_build_status.

        Returns elements with explicit fields: element_id, element_type, text, markdown,
        html, img_base64 (optional), position, page_number, bounding_box, page_layout,
        etc.

        **Query parameters:**

        - **file_id** (str, required): Unique identifier of the source.
        - **page** (int, optional): 1-based page number. Use with page_size to enable
          pagination.
        - **page_size** (int, optional): Number of elements per page (max 100).
        - **suppress_img_base64** (bool, default false): When true, img_base64 is
          omitted from each element.
        - **type** (str, optional): Filter by element type (e.g. NarrativeText, Title,
          Table).
        - **page_numbers** (list, optional): Restrict to specific page numbers (repeat
          param for multiple).
        - **element_ids** (list, optional): Restrict to specific partition element_ids
          (repeat param for multiple).
        - **elementsToRemove** (list, optional): Element types to exclude (repeat param
          for multiple).

        **Returns** Paginated response with items as BuildStatusElement list (same shape
        as GET /builds/{build_id} elements).

        Args:
          file_id: Unique identifier of the source

          element_ids: Restrict to specific element IDs (repeat param for multiple)

          elements_to_remove: Element types to exclude

          page: 1-based page number (use with page_size)

          page_numbers: Restrict to specific page numbers

          page_size: Number of elements per page

          suppress_img_base64: When true, img_base64 is omitted from each element

          type: Filter by element type (e.g. NarrativeText, Title)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sources/get-elements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "file_id": file_id,
                        "element_ids": element_ids,
                        "elements_to_remove": elements_to_remove,
                        "page": page,
                        "page_numbers": page_numbers,
                        "page_size": page_size,
                        "suppress_img_base64": suppress_img_base64,
                        "type": type,
                    },
                    source_get_elements_params.SourceGetElementsParams,
                ),
            ),
            cast_to=SourceGetElementsResponse,
        )

    async def get_page_screenshot(
        self,
        page_number: int,
        *,
        file_id: str,
        max_width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetPageScreenshotResponse:
        """
        Render a single page of a source file as a base64-encoded PNG screenshot.

        Use this endpoint to lazily fetch the visual preview of a citation returned by
        `/ask-sources` without paying the payload cost of inlining base64 in the answer.
        Supports PDFs, image files (`page_number` must be 1), and Office documents
        (doc/docx/ppt/pptx/odt — rendered from the converted PDF).

        **Path parameters:**

        - **file_id** (str): UUID of the source file.
        - **page_number** (int): 1-based page number.

        **Query parameters:**

        - **max_width** (int, optional, default `900`): Pixel width cap. Clamped to the
          300-1600 range.

        **Returns** a `PublicPageScreenshotResponse` containing:

        - `file_id`, `file_name`, `page_number` — identifying metadata.
        - `mime_type` — always `"image/png"`.
        - `width`, `height` — rendered image dimensions in pixels.
        - `image_base64` — the base64-encoded PNG bytes.

        **Error responses:**

        - `404` — File not found, unsupported file type, or invalid page number.
        - `500` — Unexpected internal error while rendering.

        Args:
          max_width: Pixel width cap for the rendered image (clamped to 300-1600).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template(
                "/sources/{file_id}/pages/{page_number}/screenshot", file_id=file_id, page_number=page_number
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"max_width": max_width}, source_get_page_screenshot_params.SourceGetPageScreenshotParams
                ),
            ),
            cast_to=SourceGetPageScreenshotResponse,
        )

    async def index_build(
        self,
        *,
        file_id: str,
        build_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIndexBuildResponse:
        """
        Build the retrieval index for an existing build from its already-parsed
        partitions — the way out of `indexing=none` without paying for a re-parse.

        Chunks, embeds and indexes the build's persisted partitions, makes it the file's
        active build, and flips the persisted `indexing` level to `full`. After it
        returns, `ask-sources`, `run-extraction` and `prebuilt-rag` see the source, and
        build status reports `searchable: true`.

        **Parameters (JSON body):**

        - **file_id** (str, required): Unique identifier of the source file.
        - **build_id** (str, optional): Build to index. Omitted → the file's active
          build. A non-active build becomes active (only the active build can serve
          retrieval).

        Synchronous: the response arrives when indexing finishes. For large documents
        the connection is kept alive with whitespace heartbeats — JSON parsers ignore
        them, no client change needed.

        **Returns** `PublicIndexBuildResponse` with `chunks_indexed`.

        Args:
          file_id: Unique identifier of the source file.

          build_id: Build to index. Omitted → the file's active build. When given, that build
              becomes the active one (only the active build can serve retrieval).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/index",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "build_id": build_id,
                },
                source_index_build_params.SourceIndexBuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIndexBuildResponse,
        )

    async def ingest_file(
        self,
        *,
        file: FileTypes,
        enrichment: Optional[str] | Omit = omit,
        folder: str | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        method: Optional[Method] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestFileResponse:
        """
        Upload a local file and schedule ingestion in the background.

        Validates the file's size and extension, stores it, then schedules the full
        data-ingestion pipeline in the background. Returns with a `build_id` to poll
        for status. Files above the direct upload limit (30 MiB) are sent in chunks
        that resume after a network error, which can take a while for a large file;
        `timeout` then applies to each request, not to the whole upload.

        **Parameters:**

        - **file** (`multipart/form-data`): The file to upload. Must include
          `Content-Length` and have a supported extension (pdf, doc, docx, csv, txt, md,
          etc.).
        - **method** (`form`, optional): Partitioning strategy. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`, `auto`. Default when omitted.
        - **enrichment** (`form`, optional): `full` (default) or `none`. `none` skips
          LLM page/section/document annotation for faster, cheaper parsing.
        - **indexing** (`form`, optional): `full` (default) or `none`. `none` skips
          chunking/embedding/indexing — the source is parsed but not searchable via
          ask/extract/retrieve. Check `GET /v2/sources/config` for availability.
        - **folder** (`form`, optional): The folder to store the source in; empty, `/`
          or omitted is the top level.

        **Returns** `AsyncIngestResponse` with `build_id`. Use it to check processing
        status.

        Args:
          enrichment: LLM enrichment level: 'full' (default) or 'none' to skip page/section/document
              annotation for faster parsing.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); empty, '/' or omitted is the top level. A folder that does
              not exist is created. An invalid path answers 400. For a file sent through an
              upload session the folder is fixed when the session starts, and the upload
              stops with `FolderScopeNotAppliedError`, before any byte is sent, if the API
              does not confirm it, or if the API offers no upload sessions (then it does not
              support folders either).

          indexing: Retrieval indexing level: 'full' (default) or 'none' to skip
              chunking/embedding/indexing — the source is parsed but not searchable. Requires
              Temporal ingestion.

          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm
              - auto → auto

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        file, large = await async_prepare_upload(file)

        async def direct() -> SourceIngestFileResponse:
            rewind(file)
            body = deepcopy_with_paths(
                {
                    "file": file,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                    "method": method,
                },
                [["file"]],
            )
            files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
            return await self._post(
                "/sources/ingest-file",
                body=await async_maybe_transform(body, source_ingest_file_params.SourceIngestFileParams),
                files=files,
                options=make_request_options(
                    extra_headers=headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceIngestFileResponse,
            )

        if large is None:
            return await direct()
        # Above the direct upload limit: an upload session (see `_large_upload`).
        return cast(
            SourceIngestFileResponse,
            await async_upload(
                self,
                large,
                direct=direct,
                method=method,
                enrichment=enrichment,
                indexing=indexing,
                folder=folder,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def ingest_github(
        self,
        *,
        url: str,
        enrichment: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestGitHubResponse:
        """
        Ingest a GitHub repository as a source into the project's knowledge graph.

        Schedules the ingestion in the background and returns immediately with a
        `build_id`. Use the returned `build_id` to poll for processing status.

        **Parameters (JSON body):**

        - **url** (str, required): The GitHub repository URL to ingest (e.g.
          `https://github.com/owner/repo`).

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          url: The GitHub repository URL to ingest (e.g. https://github.com/owner/repo)

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); an empty string or '/' is the top level. A folder that does
              not exist is created. When omitted, a new source goes to the top level and a
              source that replaces one of the same name keeps that source's folder.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/ingest-github",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                },
                source_ingest_github_params.SourceIngestGitHubParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestGitHubResponse,
        )

    async def ingest_url(
        self,
        *,
        url: str,
        crawl_urls: bool | Omit = omit,
        enrichment: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        method: Optional[Method] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestURLResponse:
        """
        Ingest a web page (or a set of crawled pages) as a source into the project's
        knowledge graph.

        Unlike the synchronous version, this endpoint schedules the ingestion in the
        background and returns immediately with a `processing` status. The source will
        be fully available once background processing completes.

        If the URL points directly to a downloadable file (detected via URL path
        extension or HTTP Content-Type), the file is first downloaded and uploaded to
        storage synchronously, then the partition/embedding pipeline runs in the
        background.

        **Parameters (JSON body):**

        - **url** (str, required): The web page URL to ingest.
        - **crawlUrls** (bool, optional, default `false`): When `true`, the system will
          also follow and ingest links found on the page. Ignored when the URL resolves
          to a file.
        - **method** (str, optional): The partitioning strategy to use. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`, `auto`. When omitted the system
          default is applied.

        **Returns** a `PublicSourceResponse` with `status: "processing"` immediately.
        Poll the source status endpoint using the returned `file_id` to track
        completion.

        **Error responses:**

        - `400` — Unsupported file type detected from a file URL.
        - `500` — Unexpected internal error during URL processing.

        Args:
          url: The web page URL to ingest

          crawl_urls: When true, also follows and ingests links found on the page

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); an empty string or '/' is the top level. A folder that does
              not exist is created. When omitted, a new source goes to the top level and a
              source that replaces one of the same name keeps that source's folder.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm
              - auto → auto

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/ingest-url",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "crawl_urls": crawl_urls,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                    "method": method,
                },
                source_ingest_url_params.SourceIngestURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestURLResponse,
        )

    async def ingest_youtube(
        self,
        *,
        url: str,
        enrichment: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceIngestYoutubeResponse:
        """
        Ingest a YouTube video as a source into the project's knowledge graph.

        Schedules the ingestion in the background and returns immediately with a
        `build_id`. The endpoint will download the transcript/captions and process them
        in the background. Use the returned `build_id` to poll for processing status.

        **Parameters (JSON body):**

        - **url** (str, required): The YouTube video URL to ingest (e.g.
          `https://www.youtube.com/watch?v=...`).

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          url: The YouTube video URL to ingest (e.g.
              https://www.youtube.com/watch?v=dQw4w9WgXcQ)

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          folder: Folder to store the source in, as a '/'-separated path (e.g.
              `Contracts/2026`); an empty string or '/' is the top level. A folder that does
              not exist is created. When omitted, a new source goes to the top level and a
              source that replaces one of the same name keeps that source's folder.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/ingest-youtube",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "enrichment": enrichment,
                    "folder": folder,
                    "indexing": indexing,
                },
                source_ingest_youtube_params.SourceIngestYoutubeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestYoutubeResponse,
        )

    async def reprocess(
        self,
        *,
        file_id: str,
        enrichment: Optional[str] | Omit = omit,
        indexing: Optional[str] | Omit = omit,
        method: Method | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceReprocessResponse:
        """
        Re-process (re-parse) an existing source in the background.

        Schedules the data-ingestion pipeline (partitioning, chunking, embedding) for an
        existing source and returns immediately with a `build_id`. Use it to poll for
        status.

        **Parameters (JSON body):**

        - **file_id** (str, required): Unique identifier of the source to re-process.
        - **method** (str, default `"fast"`): Partitioning strategy. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`, `auto`.

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          file_id: Unique identifier of the source to re-process.

          enrichment: LLM enrichment level. `full` (default) runs page/section and document
              annotation; `none` returns parsing results only and is faster, at the cost of
              weaker retrieval context.

          indexing: Retrieval indexing level. `full` (default) chunks, embeds and indexes the
              source; `none` skips it — the source will NOT be searchable via
              ask/extract/retrieve, though its parsed elements remain readable. Reversible by
              re-processing.

          method: Partitioning strategy. One of: fast, balanced, accurate, agentic, auto.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/reprocess",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "enrichment": enrichment,
                    "indexing": indexing,
                    "method": method,
                },
                source_reprocess_params.SourceReprocessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceReprocessResponse,
        )

    async def retrieve_chunks(
        self,
        *,
        query: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
        folders: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRetrieveChunksResponse:
        """
        Retrieve relevant document chunks from the prebuilt RAG vector store.

        Performs a semantic similarity search over the project's prebuilt RAG store
        using Google File Search with grounding. Returns the most relevant text chunks
        along with their source metadata (file name, page number, relevance score). This
        is a pure retrieval endpoint — it does **not** generate an answer; use
        `/ask-sources` for Q&A.

        **Parameters (JSON body):**

        - **query** (str, required): The natural-language search query used to find
          relevant chunks.
        - **file_ids** (list[str], optional — preferred): Restrict retrieval to specific
          source file IDs.
        - **file_names** (list[str], optional — deprecated): Restrict retrieval to
          specific source file names. Use `file_ids` when possible.
        - **folders** (list[str], optional): Restrict the scope to every source at or
          below each folder, together with `file_ids`. An empty list is no folder scope.

        **Returns** a `PublicRetrieveResponse` containing:

        - `query` — the original search query.
        - `chunks` — a list of `PublicRetrieveChunk` objects, each with `text`,
          `file_name`, `page_number`, `score`, and additional `metadata`.
        - `total` — the total number of chunks returned.

        **Error responses:**

        - `500` — Unexpected internal error during retrieval.

        Args:
          query: The natural-language search query to find relevant chunks

          file_ids: Optional list of file IDs to restrict retrieval scope (preferred)

          file_names: Optional list of file names to restrict retrieval scope (deprecated, use
              file_ids)

          folders: Folders to restrict the scope to (at most 1,000): every source at or below
              each folder, read when the request arrives, together with any `file_ids`. An
              empty list is no folder scope. A folder that holds no source answers 400
              `chat.folder_scope_empty`; the top level, an invalid path, or `folders` with
              `file_names` answers 422. When `folders` is not empty and the answer does not
              echo it, the API did not apply it and `FolderScopeNotAppliedError` is raised
              instead of returning the result; a failure streamed after the answer started
              raises the error for its status. Both checks run when the result is parsed,
              also through `.with_raw_response` and `.with_streaming_response` (`.parse()`),
              but not on the raw bytes (`.http_response`, `.read()`, `.text()`, `.json()`)
              nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A `folders`
              that is not a list (a string, for example) is refused before any request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        check_folders_arg(folders)
        return await self._post(
            "/sources/prebuilt-rag",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "folders": folders,
                },
                source_retrieve_chunks_params.SourceRetrieveChunksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=scope_check(self._client, "POST", "/sources/prebuilt-rag")
                if scope_sends_folders(folders)
                else not_given,
            ),
            cast_to=SourceRetrieveChunksResponse,
        )

    async def list_folders(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListFoldersResponse:
        """
        List every folder of the project, sorted, each with the folders above it.

        Lists folders created empty, folders that hold sources and folders uploads
        are on their way to. At most 10,000 folders are returned, in sort order;
        `truncated` is true when the project has more.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        try:
            return await self._get(
                "/sources/folders",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceListFoldersResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "GET /sources/folders")
            raise

    async def create_folder(
        self,
        *,
        folder: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceCreateFolderResponse:
        """
        Create a folder that stays listed while it is empty, with the folders above it.

        Safe to repeat: `created` is false when the folder existed. An upload or a
        move into a folder that does not exist creates it, so this is needed only for
        an empty folder.

        **Error responses:**

        - `409` — `folder.too_many`: the project holds the most folders it can.
        - `422` — Invalid path, or the top level.
        - `503` — The folder could not be saved; retry.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder's path, '/'-separated (for example `Contracts/2026`). Not the
              top level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        try:
            return await self._post(
                "/sources/create-folder",
                body=await async_maybe_transform(
                    {"folder": folder}, source_create_folder_params.SourceCreateFolderParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceCreateFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/create-folder")
            raise

    async def rename_folder(
        self,
        *,
        folder: str,
        new_folder: str,
        merge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRenameFolderResponse:
        """
        Rename a folder, or move it under another folder, with everything in it.

        **Not safe to repeat blindly.** After a 503, a timeout or a lost answer the
        change may have been saved, and a repeat can answer 404 `folder.not_found`
        although the first call worked. So this method never retries on its own,
        whatever `max_retries` says on the client or in `with_options`: call
        `list_folders()` and repeat by hand only if the change is not there. Only a
        404 whose `code` is `folder.not_found` may mean an earlier call worked.

        **Error responses:**

        - `400` — `folder.into_itself` (a folder into its own subfolder) or
          `folder.path_too_long` (a moved path breaks the path rules).
        - `404` — `folder.not_found`.
        - `409` — `folder.exists`: `new_folder` exists and `merge` is not set.
        - `422` — Invalid path, or the top level.
        - `503` — The change may or may not have been saved; list the folders before
          repeating.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder to rename

          new_folder: Its new path; it may sit under another folder

          merge: Merge into `new_folder` when it already exists, instead of answering 409
              `folder.exists`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        options["max_retries"] = 0  # never repeated on its own: see above
        try:
            return await self._post(
                "/sources/rename-folder",
                body=await async_maybe_transform(
                    {
                        "folder": folder,
                        "new_folder": new_folder,
                        "merge": merge,
                    },
                    source_rename_folder_params.SourceRenameFolderParams,
                ),
                options=options,
                cast_to=SourceRenameFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/rename-folder")
            raise

    async def remove_folder(
        self,
        *,
        folder: str,
        merge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRemoveFolderResponse:
        """
        Remove a folder and move its sources and subfolders into the folder above it
        (the top level for a top-level folder).

        **Not safe to repeat blindly.** After a 503, a timeout or a lost answer the
        change may have been saved, and a repeat can answer 404 `folder.not_found`
        although the first call worked. So this method never retries on its own,
        whatever `max_retries` says on the client or in `with_options`: call
        `list_folders()` and repeat by hand only if the change is not there. Only a
        404 whose `code` is `folder.not_found` may mean an earlier call worked.

        **Error responses:**

        - `404` — `folder.not_found`.
        - `409` — `folder.exists`: a subfolder has the name of a folder above and
          `merge` is not set.
        - `422` — Invalid path, or the top level.
        - `503` — The change may or may not have been saved; list the folders before
          repeating.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder to remove

          merge: Merge a subfolder into a folder of the same name above it, instead of
              answering 409 `folder.exists`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        options["max_retries"] = 0  # never repeated on its own: see above
        try:
            return await self._post(
                "/sources/remove-folder",
                body=await async_maybe_transform(
                    {
                        "folder": folder,
                        "merge": merge,
                    },
                    source_remove_folder_params.SourceRemoveFolderParams,
                ),
                options=options,
                cast_to=SourceRemoveFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/remove-folder")
            raise

    async def delete_folder(
        self,
        *,
        folder: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteFolderResponse:
        """
        Delete an empty folder and the empty folders below it.

        Its sources must be moved (`move`) or deleted first.

        **Not safe to repeat blindly.** After a 503, a timeout or a lost answer the
        change may have been saved, and a repeat can answer 404 `folder.not_found`
        although the first call worked. So this method never retries on its own,
        whatever `max_retries` says on the client or in `with_options`: call
        `list_folders()` and repeat by hand only if the change is not there. Only a
        404 whose `code` is `folder.not_found` may mean an earlier call worked.

        **Error responses:**

        - `404` — `folder.not_found`.
        - `409` — `folder.not_empty` (it holds a source) or `folder.uploads_pending`
          (uploads into it are not stored yet).
        - `422` — Invalid path, or the top level.
        - `503` — The change may or may not have been saved; list the folders before
          repeating.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          folder: The folder to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        options["max_retries"] = 0  # never repeated on its own: see above
        try:
            return await self._post(
                "/sources/delete-folder",
                body=await async_maybe_transform(
                    {"folder": folder}, source_delete_folder_params.SourceDeleteFolderParams
                ),
                options=options,
                cast_to=SourceDeleteFolderResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/delete-folder")
            raise

    async def move(
        self,
        *,
        file_ids: SequenceNotStr[str],
        folder: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceMoveResponse:
        """
        Move up to 1,000 sources to a folder.

        `""` or `/` is the top level. A folder that does not exist is created. Ids
        that match no source of the project come back in `not_found`. Safe to
        repeat.

        **Error responses:**

        - `409` — `folder.too_many`: the project holds the most folders it can.
        - `422` — Invalid path, or no ids or more than 1,000.
        - `503` — The sources could not be moved; retry.

        A 404 without an error `code` means the API does not offer this route; it
        raises `FolderScopeNotAppliedError`.

        Args:
          file_ids: The sources to move (1 to 1,000)

          folder: The target folder, '/'-separated; an empty string or '/' is the top level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        try:
            return await self._post(
                "/sources/move-sources",
                body=await async_maybe_transform(
                    {
                        "file_ids": file_ids,
                        "folder": folder,
                    },
                    source_move_params.SourceMoveParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=SourceMoveResponse,
            )
        except NotFoundError as e:
            raise_if_route_not_offered(e, "POST /sources/move-sources")
            raise


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.delete = to_raw_response_wrapper(
            sources.delete,
        )
        self.ask = to_raw_response_wrapper(
            sources.ask,
        )
        self.extract = to_raw_response_wrapper(
            sources.extract,
        )
        self.get_build_status = to_raw_response_wrapper(
            sources.get_build_status,
        )
        self.get_elements = to_raw_response_wrapper(
            sources.get_elements,
        )
        self.get_page_screenshot = to_raw_response_wrapper(
            sources.get_page_screenshot,
        )
        self.index_build = to_raw_response_wrapper(
            sources.index_build,
        )
        self.ingest_file = to_raw_response_wrapper(
            sources.ingest_file,
        )
        self.ingest_github = to_raw_response_wrapper(
            sources.ingest_github,
        )
        self.ingest_url = to_raw_response_wrapper(
            sources.ingest_url,
        )
        self.ingest_youtube = to_raw_response_wrapper(
            sources.ingest_youtube,
        )
        self.reprocess = to_raw_response_wrapper(
            sources.reprocess,
        )
        self.retrieve_chunks = to_raw_response_wrapper(
            sources.retrieve_chunks,
        )
        self.list_folders = to_raw_response_wrapper(
            sources.list_folders,
        )
        self.create_folder = to_raw_response_wrapper(
            sources.create_folder,
        )
        self.rename_folder = to_raw_response_wrapper(
            sources.rename_folder,
        )
        self.remove_folder = to_raw_response_wrapper(
            sources.remove_folder,
        )
        self.delete_folder = to_raw_response_wrapper(
            sources.delete_folder,
        )
        self.move = to_raw_response_wrapper(
            sources.move,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sources.delete,
        )
        self.ask = async_to_raw_response_wrapper(
            sources.ask,
        )
        self.extract = async_to_raw_response_wrapper(
            sources.extract,
        )
        self.get_build_status = async_to_raw_response_wrapper(
            sources.get_build_status,
        )
        self.get_elements = async_to_raw_response_wrapper(
            sources.get_elements,
        )
        self.get_page_screenshot = async_to_raw_response_wrapper(
            sources.get_page_screenshot,
        )
        self.index_build = async_to_raw_response_wrapper(
            sources.index_build,
        )
        self.ingest_file = async_to_raw_response_wrapper(
            sources.ingest_file,
        )
        self.ingest_github = async_to_raw_response_wrapper(
            sources.ingest_github,
        )
        self.ingest_url = async_to_raw_response_wrapper(
            sources.ingest_url,
        )
        self.ingest_youtube = async_to_raw_response_wrapper(
            sources.ingest_youtube,
        )
        self.reprocess = async_to_raw_response_wrapper(
            sources.reprocess,
        )
        self.retrieve_chunks = async_to_raw_response_wrapper(
            sources.retrieve_chunks,
        )
        self.list_folders = async_to_raw_response_wrapper(
            sources.list_folders,
        )
        self.create_folder = async_to_raw_response_wrapper(
            sources.create_folder,
        )
        self.rename_folder = async_to_raw_response_wrapper(
            sources.rename_folder,
        )
        self.remove_folder = async_to_raw_response_wrapper(
            sources.remove_folder,
        )
        self.delete_folder = async_to_raw_response_wrapper(
            sources.delete_folder,
        )
        self.move = async_to_raw_response_wrapper(
            sources.move,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            sources.delete,
        )
        self.ask = to_streamed_response_wrapper(
            sources.ask,
        )
        self.extract = to_streamed_response_wrapper(
            sources.extract,
        )
        self.get_build_status = to_streamed_response_wrapper(
            sources.get_build_status,
        )
        self.get_elements = to_streamed_response_wrapper(
            sources.get_elements,
        )
        self.get_page_screenshot = to_streamed_response_wrapper(
            sources.get_page_screenshot,
        )
        self.index_build = to_streamed_response_wrapper(
            sources.index_build,
        )
        self.ingest_file = to_streamed_response_wrapper(
            sources.ingest_file,
        )
        self.ingest_github = to_streamed_response_wrapper(
            sources.ingest_github,
        )
        self.ingest_url = to_streamed_response_wrapper(
            sources.ingest_url,
        )
        self.ingest_youtube = to_streamed_response_wrapper(
            sources.ingest_youtube,
        )
        self.reprocess = to_streamed_response_wrapper(
            sources.reprocess,
        )
        self.retrieve_chunks = to_streamed_response_wrapper(
            sources.retrieve_chunks,
        )
        self.list_folders = to_streamed_response_wrapper(
            sources.list_folders,
        )
        self.create_folder = to_streamed_response_wrapper(
            sources.create_folder,
        )
        self.rename_folder = to_streamed_response_wrapper(
            sources.rename_folder,
        )
        self.remove_folder = to_streamed_response_wrapper(
            sources.remove_folder,
        )
        self.delete_folder = to_streamed_response_wrapper(
            sources.delete_folder,
        )
        self.move = to_streamed_response_wrapper(
            sources.move,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sources.delete,
        )
        self.ask = async_to_streamed_response_wrapper(
            sources.ask,
        )
        self.extract = async_to_streamed_response_wrapper(
            sources.extract,
        )
        self.get_build_status = async_to_streamed_response_wrapper(
            sources.get_build_status,
        )
        self.get_elements = async_to_streamed_response_wrapper(
            sources.get_elements,
        )
        self.get_page_screenshot = async_to_streamed_response_wrapper(
            sources.get_page_screenshot,
        )
        self.index_build = async_to_streamed_response_wrapper(
            sources.index_build,
        )
        self.ingest_file = async_to_streamed_response_wrapper(
            sources.ingest_file,
        )
        self.ingest_github = async_to_streamed_response_wrapper(
            sources.ingest_github,
        )
        self.ingest_url = async_to_streamed_response_wrapper(
            sources.ingest_url,
        )
        self.ingest_youtube = async_to_streamed_response_wrapper(
            sources.ingest_youtube,
        )
        self.reprocess = async_to_streamed_response_wrapper(
            sources.reprocess,
        )
        self.retrieve_chunks = async_to_streamed_response_wrapper(
            sources.retrieve_chunks,
        )
        self.list_folders = async_to_streamed_response_wrapper(
            sources.list_folders,
        )
        self.create_folder = async_to_streamed_response_wrapper(
            sources.create_folder,
        )
        self.rename_folder = async_to_streamed_response_wrapper(
            sources.rename_folder,
        )
        self.remove_folder = async_to_streamed_response_wrapper(
            sources.remove_folder,
        )
        self.delete_folder = async_to_streamed_response_wrapper(
            sources.delete_folder,
        )
        self.move = async_to_streamed_response_wrapper(
            sources.move,
        )
