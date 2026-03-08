# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    source_ask_params,
    source_list_params,
    source_delete_params,
    source_extract_params,
    source_retrieve_chunks_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.source_ask_response import SourceAskResponse
from ..types.source_list_response import SourceListResponse
from ..types.source_delete_response import SourceDeleteResponse
from ..types.source_extract_response import SourceExtractResponse
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
        self.retrieve_chunks = async_to_streamed_response_wrapper(
            sources.retrieve_chunks,
        )
