# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    Method,
    source_ask_params,
    source_list_params,
    source_delete_params,
    source_extract_params,
    source_reprocess_params,
    source_ingest_url_params,
    source_ingest_file_params,
    source_get_elements_params,
    source_ingest_github_params,
    source_ingest_youtube_params,
    source_retrieve_chunks_params,
    source_get_build_status_params,
    source_get_page_screenshot_params,
)
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.method import Method
from ..types.source_ask_response import SourceAskResponse
from ..types.source_list_response import SourceListResponse
from ..types.source_delete_response import SourceDeleteResponse
from ..types.source_extract_response import SourceExtractResponse
from ..types.source_reprocess_response import SourceReprocessResponse
from ..types.source_ingest_url_response import SourceIngestURLResponse
from ..types.source_ingest_file_response import SourceIngestFileResponse
from ..types.source_get_elements_response import SourceGetElementsResponse
from ..types.source_ingest_github_response import SourceIngestGitHubResponse
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

        **Status messages returned per source:**

        - `"completed"` → _"Source processed successfully"_
        - `"processing"` → _"Source is being processed"_
        - `"failed"` → _"Source processing failed"_

        **Returns** a JSON array of `PublicSourceResponse` objects.

        **Error responses:**

        - `500` — Unexpected internal error while retrieving sources.

        Args:
          file_ids: Optional list of file_id to filter by (only these sources are returned). Repeat
              the param for multiple IDs.

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
                query=maybe_transform({"file_ids": file_ids}, source_list_params.SourceListParams),
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

        This is the primary Q&A endpoint. It sends the question through the GenAI File
        Search pipeline, which retrieves relevant chunks from the knowledge graph,
        grounds the answer in the source documents, and returns a natural-language
        response. Optionally, you can request a structured JSON output by supplying an
        `output_schema`.

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

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/ask-sources",
            body=maybe_transform(
                {
                    "question": question,
                    "conversation_id": conversation_id,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "include_citation_images": include_citation_images,
                    "include_citation_markup": include_citation_markup,
                    "output_schema": output_schema,
                    "reset": reset,
                    "thinking_level": thinking_level,
                },
                source_ask_params.SourceAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceAskResponse,
        )

    def extract(
        self,
        *,
        output_schema: Dict[str, object],
        user_instruction: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
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

        This endpoint uses the GenAI File Search pipeline to read the specified sources,
        apply the user-provided instruction, and return structured JSON output
        conforming to the supplied `output_schema`. Internally it builds a grounded
        prompt, queries the model, and validates/corrects the raw JSON against the
        schema.

        **Parameters (JSON body):**

        - **file_ids** (list[str], optional — preferred): List of source file IDs to
          extract from.
        - **file_names** (list[str], optional — deprecated): List of source file names
          to extract from. Use `file_ids` when possible. At least one of the two lists
          must be provided and non-empty.
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

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/run-extraction",
            body=maybe_transform(
                {
                    "output_schema": output_schema,
                    "user_instruction": user_instruction,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "thinking_level": thinking_level,
                },
                source_extract_params.SourceExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceExtractResponse,
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

    def ingest_file(
        self,
        *,
        file: FileTypes,
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

        Accepts **`multipart/form-data`** with the file. Validates size (max 100 MB) and
        extension, stores the file, then schedules the full data-ingestion pipeline in
        the background. Returns immediately with a `build_id` to poll for status.

        **Parameters:**

        - **file** (`multipart/form-data`): The file to upload. Must include
          `Content-Length` and have a supported extension (pdf, doc, docx, csv, txt, md,
          etc.).
        - **method** (`form`, optional): Partitioning strategy. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`. Default when omitted.

        **Returns** `AsyncIngestResponse` with `build_id`. Use it to check processing
        status.

        Args:
          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "method": method,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/sources/ingest-file",
            body=maybe_transform(body, source_ingest_file_params.SourceIngestFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestFileResponse,
        )

    def ingest_github(
        self,
        *,
        url: str,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/ingest-github",
            body=maybe_transform({"url": url}, source_ingest_github_params.SourceIngestGitHubParams),
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
          `balanced`, `accurate`, `vlm`, `agentic`. When omitted the system default is
          applied.

        **Returns** a `PublicSourceResponse` with `status: "processing"` immediately.
        Poll the source status endpoint using the returned `file_id` to track
        completion.

        **Error responses:**

        - `400` — Unsupported file type detected from a file URL.
        - `500` — Unexpected internal error during URL processing.

        Args:
          url: The web page URL to ingest

          crawl_urls: When true, also follows and ingests links found on the page

          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/ingest-youtube",
            body=maybe_transform({"url": url}, source_ingest_youtube_params.SourceIngestYoutubeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestYoutubeResponse,
        )

    def reprocess(
        self,
        *,
        file_id: str,
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
          `balanced`, `accurate`, `vlm`, `agentic`.

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          file_id: Unique identifier of the source to re-process.

          method: Partitioning strategy. One of: fast, balanced, accurate, agentic.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/prebuilt-rag",
            body=maybe_transform(
                {
                    "query": query,
                    "file_ids": file_ids,
                    "file_names": file_names,
                },
                source_retrieve_chunks_params.SourceRetrieveChunksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceRetrieveChunksResponse,
        )


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

        **Status messages returned per source:**

        - `"completed"` → _"Source processed successfully"_
        - `"processing"` → _"Source is being processed"_
        - `"failed"` → _"Source processing failed"_

        **Returns** a JSON array of `PublicSourceResponse` objects.

        **Error responses:**

        - `500` — Unexpected internal error while retrieving sources.

        Args:
          file_ids: Optional list of file_id to filter by (only these sources are returned). Repeat
              the param for multiple IDs.

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
                query=await async_maybe_transform({"file_ids": file_ids}, source_list_params.SourceListParams),
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

        This is the primary Q&A endpoint. It sends the question through the GenAI File
        Search pipeline, which retrieves relevant chunks from the knowledge graph,
        grounds the answer in the source documents, and returns a natural-language
        response. Optionally, you can request a structured JSON output by supplying an
        `output_schema`.

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

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/ask-sources",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "conversation_id": conversation_id,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "include_citation_images": include_citation_images,
                    "include_citation_markup": include_citation_markup,
                    "output_schema": output_schema,
                    "reset": reset,
                    "thinking_level": thinking_level,
                },
                source_ask_params.SourceAskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceAskResponse,
        )

    async def extract(
        self,
        *,
        output_schema: Dict[str, object],
        user_instruction: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        file_names: Optional[SequenceNotStr[str]] | Omit = omit,
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

        This endpoint uses the GenAI File Search pipeline to read the specified sources,
        apply the user-provided instruction, and return structured JSON output
        conforming to the supplied `output_schema`. Internally it builds a grounded
        prompt, queries the model, and validates/corrects the raw JSON against the
        schema.

        **Parameters (JSON body):**

        - **file_ids** (list[str], optional — preferred): List of source file IDs to
          extract from.
        - **file_names** (list[str], optional — deprecated): List of source file names
          to extract from. Use `file_ids` when possible. At least one of the two lists
          must be provided and non-empty.
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

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced',
              'accurate', or 'max' (most thorough)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/run-extraction",
            body=await async_maybe_transform(
                {
                    "output_schema": output_schema,
                    "user_instruction": user_instruction,
                    "file_ids": file_ids,
                    "file_names": file_names,
                    "thinking_level": thinking_level,
                },
                source_extract_params.SourceExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceExtractResponse,
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

    async def ingest_file(
        self,
        *,
        file: FileTypes,
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

        Accepts **`multipart/form-data`** with the file. Validates size (max 100 MB) and
        extension, stores the file, then schedules the full data-ingestion pipeline in
        the background. Returns immediately with a `build_id` to poll for status.

        **Parameters:**

        - **file** (`multipart/form-data`): The file to upload. Must include
          `Content-Length` and have a supported extension (pdf, doc, docx, csv, txt, md,
          etc.).
        - **method** (`form`, optional): Partitioning strategy. One of: `fast`,
          `balanced`, `accurate`, `vlm`, `agentic`. Default when omitted.

        **Returns** `AsyncIngestResponse` with `build_id`. Use it to check processing
        status.

        Args:
          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "method": method,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/sources/ingest-file",
            body=await async_maybe_transform(body, source_ingest_file_params.SourceIngestFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestFileResponse,
        )

    async def ingest_github(
        self,
        *,
        url: str,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/ingest-github",
            body=await async_maybe_transform({"url": url}, source_ingest_github_params.SourceIngestGitHubParams),
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
          `balanced`, `accurate`, `vlm`, `agentic`. When omitted the system default is
          applied.

        **Returns** a `PublicSourceResponse` with `status: "processing"` immediately.
        Poll the source status endpoint using the returned `file_id` to track
        completion.

        **Error responses:**

        - `400` — Unsupported file type detected from a file URL.
        - `500` — Unexpected internal error during URL processing.

        Args:
          url: The web page URL to ingest

          crawl_urls: When true, also follows and ingests links found on the page

          method: Public-facing partition method names for API v2.

              Maps to internal PartitionMethod as:

              - fast → basic
              - balanced → hi_res
              - accurate → hi_res_ft
              - agentic → graphorlm

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/ingest-youtube",
            body=await async_maybe_transform({"url": url}, source_ingest_youtube_params.SourceIngestYoutubeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIngestYoutubeResponse,
        )

    async def reprocess(
        self,
        *,
        file_id: str,
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
          `balanced`, `accurate`, `vlm`, `agentic`.

        **Returns** `AsyncIngestResponse` with `build_id`.

        Args:
          file_id: Unique identifier of the source to re-process.

          method: Partitioning strategy. One of: fast, balanced, accurate, agentic.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/prebuilt-rag",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "file_ids": file_ids,
                    "file_names": file_names,
                },
                source_retrieve_chunks_params.SourceRetrieveChunksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceRetrieveChunksResponse,
        )


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
