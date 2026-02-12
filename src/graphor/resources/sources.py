# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    PublicPartitionMethod,
    source_ask_params,
    source_parse_params,
    source_delete_params,
    source_upload_params,
    source_extract_params,
    source_upload_url_params,
    source_load_elements_params,
    source_upload_github_params,
    source_upload_youtube_params,
    source_retrieve_chunks_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.public_source import PublicSource
from ..types.source_ask_response import SourceAskResponse
from ..types.source_list_response import SourceListResponse
from ..types.source_delete_response import SourceDeleteResponse
from ..types.public_partition_method import PublicPartitionMethod
from ..types.source_extract_response import SourceExtractResponse
from ..types.source_load_elements_response import SourceLoadElementsResponse
from ..types.source_retrieve_chunks_response import SourceRetrieveChunksResponse

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

        **Status messages returned per source:**

        - `"completed"` → _"Source processed successfully"_
        - `"processing"` → _"Source is being processed"_
        - `"failed"` → _"Source processing failed"_
        - `"new"` → _"Source uploaded, awaiting processing"_

        **Returns** a JSON array of `PublicSourceResponse` objects.

        **Error responses:**

        - `500` — Unexpected internal error while retrieving sources.
        """
        return self._get(
            "/sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reset: Optional[bool] | Omit = omit,
        thinking_level: Optional[Literal["fast", "balanced", "accurate"]] | Omit = omit,
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

          output_schema: Optional JSON Schema for requesting structured output. When provided, the answer
              field will contain a short status message and the structured data will be in
              structured_output.

          reset: When true, starts a new conversation discarding any previous history

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced', or
              'accurate' (most thorough)

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
        thinking_level: Optional[Literal["fast", "balanced", "accurate"]] | Omit = omit,
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

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced', or
              'accurate' (most thorough)

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

    def load_elements(
        self,
        *,
        file_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        filter: Optional[source_load_elements_params.Filter] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceLoadElementsResponse:
        """
        Retrieve the parsed elements (chunks/partitions) of a specific source with
        pagination.

        Returns the individual document partitions (text chunks) that were generated
        during ingestion for a given source. This is useful for inspecting how a file
        was segmented, reviewing chunk content, or building custom retrieval logic on
        top of the raw partitions.

        **Parameters (JSON body):**

        - **file_id** (str, optional — preferred): The unique identifier of the source
          whose elements to retrieve.
        - **file_name** (str, optional — deprecated): The display name of the source.
          Use `file_id` when possible. At least one of `file_id` or `file_name` must be
          provided.
        - **page** (int, optional): The 1-based page number for pagination.
        - **page_size** (int, optional): The number of elements per page. Both `page`
          and `page_size` must be provided together to enable pagination.
        - **filter** (object, optional): An optional filter object with:
          - `type` — filter by element type.
          - `page_numbers` — restrict to specific source page numbers.
          - `elementsToRemove` — list of element types to exclude.

        **Returns** a `PaginatedResponse[Document]` containing:

        - `items` — list of `Document` objects (LangChain format) with `page_content`
          and `metadata`.
        - `total` — total number of matching elements.
        - `page`, `page_size`, `total_pages` — pagination metadata.

        **Error responses:**

        - `400` — Invalid input (e.g. neither identifier provided).
        - `404` — Source file not found.
        - `500` — Unexpected internal error.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          filter: Optional filter to narrow down the returned elements

          page: Current page number

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/elements",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                    "filter": filter,
                    "page": page,
                    "page_size": page_size,
                },
                source_load_elements_params.SourceLoadElementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceLoadElementsResponse,
        )

    def parse(
        self,
        *,
        file_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        partition_method: PublicPartitionMethod | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Re-process (re-parse) an existing source that has already been uploaded.

        Use this endpoint to re-run the data-ingestion pipeline on a source that is
        already present in the knowledge graph — for example, after changing the
        partitioning strategy. The endpoint locates the source node, sets its status to
        `PROCESSING`, applies the requested partition method, and executes the full
        ingestion pipeline synchronously (partitioning, chunking, embedding, and graph
        persistence).

        **Parameters (JSON body):**

        - **file_id** (str, optional — preferred): The unique identifier of the source
          to re-process.
        - **file_name** (str, optional — deprecated): The display name of the source.
          Use `file_id` instead when possible. At least one of `file_id` or `file_name`
          must be provided.
        - **partition_method** (str, default `"basic"`): The partitioning strategy to
          apply. One of: `basic` (Fast), `hi_res` (Balanced), `hi_res_ft` (Accurate),
          `mai` (VLM), `graphorlm` (Agentic).

        **Returns** a `PublicSourceResponse` with the updated source metadata.

        **Error responses:**

        - `404` — Source node not found for the given identifier.
        - `500` — Processing or unexpected internal error.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          partition_method: The partitioning strategy to apply. Available methods: basic (Fast), hi_res
              (Balanced), hi_res_ft (Accurate), mai (VLM), graphorlm (Agentic)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/process",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                    "partition_method": partition_method,
                },
                source_parse_params.SourceParseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
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

    def upload(
        self,
        *,
        file: FileTypes,
        partition_method: Optional[PublicPartitionMethod] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Upload a local file and ingest it as a source into the project's knowledge
        graph.

        This endpoint accepts a **`multipart/form-data`** request containing the file to
        upload. It validates the file size (max 100 MB) and extension against the list
        of allowed types, stores the file, and then runs the full data-ingestion
        pipeline synchronously — including partitioning, chunking, embedding, and graph
        persistence.

        **Usage via SDK (AI agent / MCP context):**

        The SDK executes code in a **remote sandboxed container** that does **not** have
        access to the local filesystem. Because of this, `fs.createReadStream()` with a
        local file path will **not work** — the file does not exist inside the
        container.

        For **text-based files** (md, txt, csv, html, etc.), you can read the file
        content with a local tool (e.g. IDE file-read) and create a `File` object in
        memory:

        ```
        const content = `...file contents read locally...`;
        const file = new File([content], "my-document.md", { type: "text/markdown" });
        const result = await client.sources.upload({ file });
        ```

        For **binary files** (pdf, docx, images, video, audio, etc.), the in-memory
        approach is impractical. Instead, use **`curl`** or **`subprocess`** to call the
        upload endpoint directly from the local machine, where the file is accessible:

        ```
        import { execSync } from "child_process";

        const result = execSync(`
          curl -s -X POST "{base_url}/source/upload" \\
            -H "Authorization: Bearer {access_key}" \\
            -F "file=@/local/path/to/document.pdf" \\
            -F "partition_method=graphorlm"
        `).toString();
        ```

        Or with Python `subprocess`:

        ```
        import subprocess, json

        result = subprocess.run([
            "curl", "-s", "-X", "POST", "{base_url}/source/upload",
            "-H", "Authorization: Bearer {access_key}",
            "-F", "file=@/local/path/to/document.pdf",
            "-F", "partition_method=graphorlm",
        ], capture_output=True, text=True)
        response = json.loads(result.stdout)
        ```

        **Important:** Do NOT use `fs.createReadStream("/local/path")` inside the SDK
        code — it will fail because the execution environment cannot access local paths.
        Always prefer `curl`/`requests` executed locally for binary uploads.

        **Usage via curl:**

        ```
        curl -X POST "{base_url}/source/upload" \\
          -H "Authorization: Bearer {access_key}" \\
          -F "file=@/path/to/document.pdf" \\
          -F "partition_method=graphorlm"
        ```

        **Usage via Python `requests`:**

        ```
        import requests

        with open("document.pdf", "rb") as f:
            response = requests.post(
                "{base_url}/source/upload",
                headers={"Authorization": "Bearer {access_key}"},
                files={"file": ("document.pdf", f, "application/pdf")},
                data={"partition_method": "graphorlm"},  # optional
            )
        ```

        **Parameters:**

        - **file** (`multipart/form-data`): The file to upload. Must include a
          `Content-Length` header and have one of the supported extensions: pdf, doc,
          docx, odt, ppt, pptx, csv, tsv, xls, xlsx, txt, text, md, html, htm, png, jpg,
          jpeg, tiff, bmp, heic, mp4, mov, avi, mkv, webm, mp3, wav, m4a, ogg, flac.
        - **partition_method** (`form`, optional): The partitioning strategy to apply.
          One of: `basic` (Fast), `hi_res` (Balanced), `hi_res_ft` (Accurate), `mai`
          (VLM), `graphorlm` (Agentic). When omitted, the system default is used.

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `400` — Unsupported file type or missing file name.
        - `411` — Missing `Content-Length` header (file size cannot be determined).
        - `413` — File exceeds the 100 MB size limit.
        - `403` — Permission denied.
        - `404` — File not found during processing.
        - `500` — Unexpected internal error.

        Args:
          partition_method: Partition methods available for public API endpoints.

              Each value also has a human-readable alias:

              - `basic` → **Fast**
              - `hi_res` → **Balanced**
              - `hi_res_ft` → **Accurate**
              - `mai` → **VLM**
              - `graphorlm` → **Agentic**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "partition_method": partition_method,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/sources/upload",
            body=maybe_transform(body, source_upload_params.SourceUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
        )

    def upload_github(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Ingest a GitHub repository as a source into the project's knowledge graph.

        The endpoint clones or fetches the repository at the given URL, extracts its
        text-based files, partitions them using the system default method, generates
        embeddings, and persists everything in the knowledge graph synchronously.

        **Parameters (JSON body):**

        - **url** (str, required): The GitHub repository URL to ingest (e.g.
          `https://github.com/owner/repo`).

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `500` — Unexpected internal error during GitHub source processing.

        Args:
          url: The GitHub repository URL to ingest (e.g. https://github.com/owner/repo)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/upload-github-source",
            body=maybe_transform({"url": url}, source_upload_github_params.SourceUploadGitHubParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
        )

    def upload_url(
        self,
        *,
        url: str,
        crawl_urls: bool | Omit = omit,
        partition_method: Optional[PublicPartitionMethod] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Ingest a web page (or a set of crawled pages) as a source into the project's
        knowledge graph.

        The endpoint fetches the content at the given URL, optionally crawls linked
        pages (when `crawlUrls` is `true`), partitions the resulting HTML/text,
        generates embeddings, and persists everything in the knowledge graph
        synchronously.

        **Parameters (JSON body):**

        - **url** (str, required): The web page URL to ingest.
        - **crawlUrls** (bool, optional, default `false`): When `true`, the system will
          also follow and ingest links found on the page.
        - **partition_method** (str, optional): The partitioning strategy to use. One
          of: `basic` (Fast), `hi_res` (Balanced), `hi_res_ft` (Accurate), `mai` (VLM),
          `graphorlm` (Agentic). When omitted the system default is applied.

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `500` — Unexpected internal error during URL processing.

        Args:
          url: The web page URL to ingest

          crawl_urls: When true, also follows and ingests links found on the page

          partition_method: Partition methods available for public API endpoints.

              Each value also has a human-readable alias:

              - `basic` → **Fast**
              - `hi_res` → **Balanced**
              - `hi_res_ft` → **Accurate**
              - `mai` → **VLM**
              - `graphorlm` → **Agentic**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/upload-url-source",
            body=maybe_transform(
                {
                    "url": url,
                    "crawl_urls": crawl_urls,
                    "partition_method": partition_method,
                },
                source_upload_url_params.SourceUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
        )

    def upload_youtube(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Ingest a YouTube video as a source into the project's knowledge graph.

        The endpoint downloads the transcript/captions of the given YouTube video,
        partitions the text using the system default method, generates embeddings, and
        persists everything in the knowledge graph synchronously.

        **Parameters (JSON body):**

        - **url** (str, required): The YouTube video URL to ingest (e.g.
          `https://www.youtube.com/watch?v=...`).

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `500` — Unexpected internal error during YouTube source processing.

        Args:
          url: The YouTube video URL to ingest (e.g.
              https://www.youtube.com/watch?v=dQw4w9WgXcQ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/upload-youtube-source",
            body=maybe_transform({"url": url}, source_upload_youtube_params.SourceUploadYoutubeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
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

        **Status messages returned per source:**

        - `"completed"` → _"Source processed successfully"_
        - `"processing"` → _"Source is being processed"_
        - `"failed"` → _"Source processing failed"_
        - `"new"` → _"Source uploaded, awaiting processing"_

        **Returns** a JSON array of `PublicSourceResponse` objects.

        **Error responses:**

        - `500` — Unexpected internal error while retrieving sources.
        """
        return await self._get(
            "/sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reset: Optional[bool] | Omit = omit,
        thinking_level: Optional[Literal["fast", "balanced", "accurate"]] | Omit = omit,
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

          output_schema: Optional JSON Schema for requesting structured output. When provided, the answer
              field will contain a short status message and the structured data will be in
              structured_output.

          reset: When true, starts a new conversation discarding any previous history

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced', or
              'accurate' (most thorough)

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
        thinking_level: Optional[Literal["fast", "balanced", "accurate"]] | Omit = omit,
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

          thinking_level: Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced', or
              'accurate' (most thorough)

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

    async def load_elements(
        self,
        *,
        file_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        filter: Optional[source_load_elements_params.Filter] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceLoadElementsResponse:
        """
        Retrieve the parsed elements (chunks/partitions) of a specific source with
        pagination.

        Returns the individual document partitions (text chunks) that were generated
        during ingestion for a given source. This is useful for inspecting how a file
        was segmented, reviewing chunk content, or building custom retrieval logic on
        top of the raw partitions.

        **Parameters (JSON body):**

        - **file_id** (str, optional — preferred): The unique identifier of the source
          whose elements to retrieve.
        - **file_name** (str, optional — deprecated): The display name of the source.
          Use `file_id` when possible. At least one of `file_id` or `file_name` must be
          provided.
        - **page** (int, optional): The 1-based page number for pagination.
        - **page_size** (int, optional): The number of elements per page. Both `page`
          and `page_size` must be provided together to enable pagination.
        - **filter** (object, optional): An optional filter object with:
          - `type` — filter by element type.
          - `page_numbers` — restrict to specific source page numbers.
          - `elementsToRemove` — list of element types to exclude.

        **Returns** a `PaginatedResponse[Document]` containing:

        - `items` — list of `Document` objects (LangChain format) with `page_content`
          and `metadata`.
        - `total` — total number of matching elements.
        - `page`, `page_size`, `total_pages` — pagination metadata.

        **Error responses:**

        - `400` — Invalid input (e.g. neither identifier provided).
        - `404` — Source file not found.
        - `500` — Unexpected internal error.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          filter: Optional filter to narrow down the returned elements

          page: Current page number

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/elements",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                    "filter": filter,
                    "page": page,
                    "page_size": page_size,
                },
                source_load_elements_params.SourceLoadElementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceLoadElementsResponse,
        )

    async def parse(
        self,
        *,
        file_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        partition_method: PublicPartitionMethod | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Re-process (re-parse) an existing source that has already been uploaded.

        Use this endpoint to re-run the data-ingestion pipeline on a source that is
        already present in the knowledge graph — for example, after changing the
        partitioning strategy. The endpoint locates the source node, sets its status to
        `PROCESSING`, applies the requested partition method, and executes the full
        ingestion pipeline synchronously (partitioning, chunking, embedding, and graph
        persistence).

        **Parameters (JSON body):**

        - **file_id** (str, optional — preferred): The unique identifier of the source
          to re-process.
        - **file_name** (str, optional — deprecated): The display name of the source.
          Use `file_id` instead when possible. At least one of `file_id` or `file_name`
          must be provided.
        - **partition_method** (str, default `"basic"`): The partitioning strategy to
          apply. One of: `basic` (Fast), `hi_res` (Balanced), `hi_res_ft` (Accurate),
          `mai` (VLM), `graphorlm` (Agentic).

        **Returns** a `PublicSourceResponse` with the updated source metadata.

        **Error responses:**

        - `404` — Source node not found for the given identifier.
        - `500` — Processing or unexpected internal error.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          partition_method: The partitioning strategy to apply. Available methods: basic (Fast), hi_res
              (Balanced), hi_res_ft (Accurate), mai (VLM), graphorlm (Agentic)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/process",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                    "partition_method": partition_method,
                },
                source_parse_params.SourceParseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
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

    async def upload(
        self,
        *,
        file: FileTypes,
        partition_method: Optional[PublicPartitionMethod] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Upload a local file and ingest it as a source into the project's knowledge
        graph.

        This endpoint accepts a **`multipart/form-data`** request containing the file to
        upload. It validates the file size (max 100 MB) and extension against the list
        of allowed types, stores the file, and then runs the full data-ingestion
        pipeline synchronously — including partitioning, chunking, embedding, and graph
        persistence.

        **Usage via SDK (AI agent / MCP context):**

        The SDK executes code in a **remote sandboxed container** that does **not** have
        access to the local filesystem. Because of this, `fs.createReadStream()` with a
        local file path will **not work** — the file does not exist inside the
        container.

        For **text-based files** (md, txt, csv, html, etc.), you can read the file
        content with a local tool (e.g. IDE file-read) and create a `File` object in
        memory:

        ```
        const content = `...file contents read locally...`;
        const file = new File([content], "my-document.md", { type: "text/markdown" });
        const result = await client.sources.upload({ file });
        ```

        For **binary files** (pdf, docx, images, video, audio, etc.), the in-memory
        approach is impractical. Instead, use **`curl`** or **`subprocess`** to call the
        upload endpoint directly from the local machine, where the file is accessible:

        ```
        import { execSync } from "child_process";

        const result = execSync(`
          curl -s -X POST "{base_url}/source/upload" \\
            -H "Authorization: Bearer {access_key}" \\
            -F "file=@/local/path/to/document.pdf" \\
            -F "partition_method=graphorlm"
        `).toString();
        ```

        Or with Python `subprocess`:

        ```
        import subprocess, json

        result = subprocess.run([
            "curl", "-s", "-X", "POST", "{base_url}/source/upload",
            "-H", "Authorization: Bearer {access_key}",
            "-F", "file=@/local/path/to/document.pdf",
            "-F", "partition_method=graphorlm",
        ], capture_output=True, text=True)
        response = json.loads(result.stdout)
        ```

        **Important:** Do NOT use `fs.createReadStream("/local/path")` inside the SDK
        code — it will fail because the execution environment cannot access local paths.
        Always prefer `curl`/`requests` executed locally for binary uploads.

        **Usage via curl:**

        ```
        curl -X POST "{base_url}/source/upload" \\
          -H "Authorization: Bearer {access_key}" \\
          -F "file=@/path/to/document.pdf" \\
          -F "partition_method=graphorlm"
        ```

        **Usage via Python `requests`:**

        ```
        import requests

        with open("document.pdf", "rb") as f:
            response = requests.post(
                "{base_url}/source/upload",
                headers={"Authorization": "Bearer {access_key}"},
                files={"file": ("document.pdf", f, "application/pdf")},
                data={"partition_method": "graphorlm"},  # optional
            )
        ```

        **Parameters:**

        - **file** (`multipart/form-data`): The file to upload. Must include a
          `Content-Length` header and have one of the supported extensions: pdf, doc,
          docx, odt, ppt, pptx, csv, tsv, xls, xlsx, txt, text, md, html, htm, png, jpg,
          jpeg, tiff, bmp, heic, mp4, mov, avi, mkv, webm, mp3, wav, m4a, ogg, flac.
        - **partition_method** (`form`, optional): The partitioning strategy to apply.
          One of: `basic` (Fast), `hi_res` (Balanced), `hi_res_ft` (Accurate), `mai`
          (VLM), `graphorlm` (Agentic). When omitted, the system default is used.

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `400` — Unsupported file type or missing file name.
        - `411` — Missing `Content-Length` header (file size cannot be determined).
        - `413` — File exceeds the 100 MB size limit.
        - `403` — Permission denied.
        - `404` — File not found during processing.
        - `500` — Unexpected internal error.

        Args:
          partition_method: Partition methods available for public API endpoints.

              Each value also has a human-readable alias:

              - `basic` → **Fast**
              - `hi_res` → **Balanced**
              - `hi_res_ft` → **Accurate**
              - `mai` → **VLM**
              - `graphorlm` → **Agentic**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "partition_method": partition_method,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/sources/upload",
            body=await async_maybe_transform(body, source_upload_params.SourceUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
        )

    async def upload_github(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Ingest a GitHub repository as a source into the project's knowledge graph.

        The endpoint clones or fetches the repository at the given URL, extracts its
        text-based files, partitions them using the system default method, generates
        embeddings, and persists everything in the knowledge graph synchronously.

        **Parameters (JSON body):**

        - **url** (str, required): The GitHub repository URL to ingest (e.g.
          `https://github.com/owner/repo`).

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `500` — Unexpected internal error during GitHub source processing.

        Args:
          url: The GitHub repository URL to ingest (e.g. https://github.com/owner/repo)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/upload-github-source",
            body=await async_maybe_transform({"url": url}, source_upload_github_params.SourceUploadGitHubParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
        )

    async def upload_url(
        self,
        *,
        url: str,
        crawl_urls: bool | Omit = omit,
        partition_method: Optional[PublicPartitionMethod] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Ingest a web page (or a set of crawled pages) as a source into the project's
        knowledge graph.

        The endpoint fetches the content at the given URL, optionally crawls linked
        pages (when `crawlUrls` is `true`), partitions the resulting HTML/text,
        generates embeddings, and persists everything in the knowledge graph
        synchronously.

        **Parameters (JSON body):**

        - **url** (str, required): The web page URL to ingest.
        - **crawlUrls** (bool, optional, default `false`): When `true`, the system will
          also follow and ingest links found on the page.
        - **partition_method** (str, optional): The partitioning strategy to use. One
          of: `basic` (Fast), `hi_res` (Balanced), `hi_res_ft` (Accurate), `mai` (VLM),
          `graphorlm` (Agentic). When omitted the system default is applied.

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `500` — Unexpected internal error during URL processing.

        Args:
          url: The web page URL to ingest

          crawl_urls: When true, also follows and ingests links found on the page

          partition_method: Partition methods available for public API endpoints.

              Each value also has a human-readable alias:

              - `basic` → **Fast**
              - `hi_res` → **Balanced**
              - `hi_res_ft` → **Accurate**
              - `mai` → **VLM**
              - `graphorlm` → **Agentic**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/upload-url-source",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "crawl_urls": crawl_urls,
                    "partition_method": partition_method,
                },
                source_upload_url_params.SourceUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
        )

    async def upload_youtube(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSource:
        """
        Ingest a YouTube video as a source into the project's knowledge graph.

        The endpoint downloads the transcript/captions of the given YouTube video,
        partitions the text using the system default method, generates embeddings, and
        persists everything in the knowledge graph synchronously.

        **Parameters (JSON body):**

        - **url** (str, required): The YouTube video URL to ingest (e.g.
          `https://www.youtube.com/watch?v=...`).

        **Returns** a `PublicSourceResponse` with the resulting source metadata (file
        ID, name, size, type, source origin, partition method, and processing status).

        **Error responses:**

        - `500` — Unexpected internal error during YouTube source processing.

        Args:
          url: The YouTube video URL to ingest (e.g.
              https://www.youtube.com/watch?v=dQw4w9WgXcQ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/upload-youtube-source",
            body=await async_maybe_transform({"url": url}, source_upload_youtube_params.SourceUploadYoutubeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSource,
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
        self.load_elements = to_raw_response_wrapper(
            sources.load_elements,
        )
        self.parse = to_raw_response_wrapper(
            sources.parse,
        )
        self.retrieve_chunks = to_raw_response_wrapper(
            sources.retrieve_chunks,
        )
        self.upload = to_raw_response_wrapper(
            sources.upload,
        )
        self.upload_github = to_raw_response_wrapper(
            sources.upload_github,
        )
        self.upload_url = to_raw_response_wrapper(
            sources.upload_url,
        )
        self.upload_youtube = to_raw_response_wrapper(
            sources.upload_youtube,
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
        self.load_elements = async_to_raw_response_wrapper(
            sources.load_elements,
        )
        self.parse = async_to_raw_response_wrapper(
            sources.parse,
        )
        self.retrieve_chunks = async_to_raw_response_wrapper(
            sources.retrieve_chunks,
        )
        self.upload = async_to_raw_response_wrapper(
            sources.upload,
        )
        self.upload_github = async_to_raw_response_wrapper(
            sources.upload_github,
        )
        self.upload_url = async_to_raw_response_wrapper(
            sources.upload_url,
        )
        self.upload_youtube = async_to_raw_response_wrapper(
            sources.upload_youtube,
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
        self.load_elements = to_streamed_response_wrapper(
            sources.load_elements,
        )
        self.parse = to_streamed_response_wrapper(
            sources.parse,
        )
        self.retrieve_chunks = to_streamed_response_wrapper(
            sources.retrieve_chunks,
        )
        self.upload = to_streamed_response_wrapper(
            sources.upload,
        )
        self.upload_github = to_streamed_response_wrapper(
            sources.upload_github,
        )
        self.upload_url = to_streamed_response_wrapper(
            sources.upload_url,
        )
        self.upload_youtube = to_streamed_response_wrapper(
            sources.upload_youtube,
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
        self.load_elements = async_to_streamed_response_wrapper(
            sources.load_elements,
        )
        self.parse = async_to_streamed_response_wrapper(
            sources.parse,
        )
        self.retrieve_chunks = async_to_streamed_response_wrapper(
            sources.retrieve_chunks,
        )
        self.upload = async_to_streamed_response_wrapper(
            sources.upload,
        )
        self.upload_github = async_to_streamed_response_wrapper(
            sources.upload_github,
        )
        self.upload_url = async_to_streamed_response_wrapper(
            sources.upload_url,
        )
        self.upload_youtube = async_to_streamed_response_wrapper(
            sources.upload_youtube,
        )
