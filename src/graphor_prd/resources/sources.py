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

        For more information, see https://www.github.com/stainless-sdks/graphor-prd-python#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/graphor-prd-python#with_streaming_response
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
        """Get the source nodes of the knowledge graph for public access."""
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
        Delete a source from the project for public access.

        Accepts either file_id (preferred) or file_name (deprecated) as identifier.

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
        Public endpoint to ask questions about the sources.

        Args:
          question: The question to ask about the sources

          conversation_id: Conversation identifier to maintain memory context

          file_ids: Optional list of file IDs to restrict search to one or more documents
              (preferred)

          file_names: Optional list of file display names to restrict search to one or more documents
              (deprecated, use file_ids)

          output_schema: Optional JSON Schema used to request a structured output. When provided, the
              system will first ask the sources model to output JSON-text, then
              validate/correct it with gemini-3-flash-preview.

          reset: When true, starts a new conversation and ignores history

          thinking_level: Controls model and thinking configuration: 'fast', 'balanced', 'accurate'

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
        Run a one-off public extraction for files using the provided output schema.

        Args:
          output_schema: JSON Schema used to request a structured output. The system will extract data
              according to this schema.

          user_instruction: User instruction to guide the extraction

          file_ids: List of file IDs to extract from (preferred)

          file_names: List of file names to extract from (deprecated, use file_ids)

          thinking_level: Controls model and thinking configuration: 'fast', 'balanced', 'accurate'

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
        Loads elements from a file with optional pagination for public access.

        Accepts either file_id (preferred) or file_name (deprecated) as identifier.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          filter: The filter of the elements

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
        Process/parse an existing source.

        Accepts either file_id (preferred) or file_name (deprecated) as identifier.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          partition_method: The method used to partition the file

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
        """Public endpoint to retrieve relevant chunks from the prebuild RAG store.

        Uses
        Google File Search with grounding to find relevant document chunks.

        Accepts either file_ids (preferred) or file_names (deprecated) as identifier.

        Args:
          query: The search query to retrieve relevant chunks

          file_ids: Optional list of file IDs to restrict retrieval to one or more documents
              (preferred)

          file_names: Optional list of file names to restrict retrieval to one or more documents
              (deprecated, use file_ids)

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
        Upload

        Args:
          partition_method: Partition methods available for public API endpoints.

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
        Public endpoint to process a source from a GitHub repository using synchronous
        ingestion.

        Args:
          url: The url of the github repository

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
        """Public endpoint to upload and process a source from a URL.

        Triggers background
        ingestion and returns immediately.

        Args:
          url: The url of the source

          crawl_urls: Whether to crawl urls from the source

          partition_method: Partition methods available for public API endpoints.

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
        Public endpoint to process a source from a YouTube video using synchronous
        ingestion.

        Args:
          url: The url of the youtube video

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

        For more information, see https://www.github.com/stainless-sdks/graphor-prd-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/graphor-prd-python#with_streaming_response
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
        """Get the source nodes of the knowledge graph for public access."""
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
        Delete a source from the project for public access.

        Accepts either file_id (preferred) or file_name (deprecated) as identifier.

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
        Public endpoint to ask questions about the sources.

        Args:
          question: The question to ask about the sources

          conversation_id: Conversation identifier to maintain memory context

          file_ids: Optional list of file IDs to restrict search to one or more documents
              (preferred)

          file_names: Optional list of file display names to restrict search to one or more documents
              (deprecated, use file_ids)

          output_schema: Optional JSON Schema used to request a structured output. When provided, the
              system will first ask the sources model to output JSON-text, then
              validate/correct it with gemini-3-flash-preview.

          reset: When true, starts a new conversation and ignores history

          thinking_level: Controls model and thinking configuration: 'fast', 'balanced', 'accurate'

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
        Run a one-off public extraction for files using the provided output schema.

        Args:
          output_schema: JSON Schema used to request a structured output. The system will extract data
              according to this schema.

          user_instruction: User instruction to guide the extraction

          file_ids: List of file IDs to extract from (preferred)

          file_names: List of file names to extract from (deprecated, use file_ids)

          thinking_level: Controls model and thinking configuration: 'fast', 'balanced', 'accurate'

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
        Loads elements from a file with optional pagination for public access.

        Accepts either file_id (preferred) or file_name (deprecated) as identifier.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          filter: The filter of the elements

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
        Process/parse an existing source.

        Accepts either file_id (preferred) or file_name (deprecated) as identifier.

        Args:
          file_id: Unique identifier for the source (preferred)

          file_name: The name of the file (deprecated, use file_id)

          partition_method: The method used to partition the file

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
        """Public endpoint to retrieve relevant chunks from the prebuild RAG store.

        Uses
        Google File Search with grounding to find relevant document chunks.

        Accepts either file_ids (preferred) or file_names (deprecated) as identifier.

        Args:
          query: The search query to retrieve relevant chunks

          file_ids: Optional list of file IDs to restrict retrieval to one or more documents
              (preferred)

          file_names: Optional list of file names to restrict retrieval to one or more documents
              (deprecated, use file_ids)

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
        Upload

        Args:
          partition_method: Partition methods available for public API endpoints.

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
        Public endpoint to process a source from a GitHub repository using synchronous
        ingestion.

        Args:
          url: The url of the github repository

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
        """Public endpoint to upload and process a source from a URL.

        Triggers background
        ingestion and returns immediately.

        Args:
          url: The url of the source

          crawl_urls: Whether to crawl urls from the source

          partition_method: Partition methods available for public API endpoints.

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
        Public endpoint to process a source from a YouTube video using synchronous
        ingestion.

        Args:
          url: The url of the youtube video

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
