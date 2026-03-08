# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from graphor import Graphor, AsyncGraphor
from tests.utils import assert_matches_type
from graphor.types import (
    SourceAskResponse,
    SourceListResponse,
    SourceDeleteResponse,
    SourceExtractResponse,
    SourceIngestURLResponse,
    SourceReprocessResponse,
    SourceIngestFileResponse,
    SourceIngestGitHubResponse,
    SourceIngestYoutubeResponse,
    SourceRetrieveChunksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Graphor) -> None:
        source = client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Graphor) -> None:
        source = client.sources.list(
            file_ids=["string"],
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Graphor) -> None:
        source = client.sources.delete()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Graphor) -> None:
        source = client.sources.delete(
            file_id="file_id",
            file_name="file_name",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceDeleteResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ask(self, client: Graphor) -> None:
        source = client.sources.ask(
            question="question",
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ask_with_all_params(self, client: Graphor) -> None:
        source = client.sources.ask(
            question="question",
            conversation_id="conversation_id",
            file_ids=["string"],
            file_names=["string"],
            output_schema={"foo": "bar"},
            reset=True,
            thinking_level="fast",
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ask(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.ask(
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ask(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.ask(
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceAskResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract(self, client: Graphor) -> None:
        source = client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: Graphor) -> None:
        source = client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
            file_ids=["string"],
            file_names=["string"],
            thinking_level="fast",
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceExtractResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_file(self, client: Graphor) -> None:
        source = client.sources.ingest_file(
            file=b"Example data",
        )
        assert_matches_type(SourceIngestFileResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_file_with_all_params(self, client: Graphor) -> None:
        source = client.sources.ingest_file(
            file=b"Example data",
            partition_method="fast",
        )
        assert_matches_type(SourceIngestFileResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_file(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.ingest_file(
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceIngestFileResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_file(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.ingest_file(
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceIngestFileResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_github(self, client: Graphor) -> None:
        source = client.sources.ingest_github(
            url="url",
        )
        assert_matches_type(SourceIngestGitHubResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_github(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.ingest_github(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceIngestGitHubResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_github(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.ingest_github(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceIngestGitHubResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_url(self, client: Graphor) -> None:
        source = client.sources.ingest_url(
            url="url",
        )
        assert_matches_type(SourceIngestURLResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_url_with_all_params(self, client: Graphor) -> None:
        source = client.sources.ingest_url(
            url="url",
            crawl_urls=True,
            partition_method="fast",
        )
        assert_matches_type(SourceIngestURLResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_url(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.ingest_url(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceIngestURLResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_url(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.ingest_url(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceIngestURLResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_youtube(self, client: Graphor) -> None:
        source = client.sources.ingest_youtube(
            url="url",
        )
        assert_matches_type(SourceIngestYoutubeResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_youtube(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.ingest_youtube(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceIngestYoutubeResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_youtube(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.ingest_youtube(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceIngestYoutubeResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reprocess(self, client: Graphor) -> None:
        source = client.sources.reprocess(
            file_id="file_id",
        )
        assert_matches_type(SourceReprocessResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reprocess_with_all_params(self, client: Graphor) -> None:
        source = client.sources.reprocess(
            file_id="file_id",
            partition_method="fast",
        )
        assert_matches_type(SourceReprocessResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reprocess(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.reprocess(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceReprocessResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reprocess(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.reprocess(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceReprocessResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_chunks(self, client: Graphor) -> None:
        source = client.sources.retrieve_chunks(
            query="query",
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_chunks_with_all_params(self, client: Graphor) -> None:
        source = client.sources.retrieve_chunks(
            query="query",
            file_ids=["string"],
            file_names=["string"],
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_chunks(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.retrieve_chunks(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_chunks(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.retrieve_chunks(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.list(
            file_ids=["string"],
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.delete()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.delete(
            file_id="file_id",
            file_name="file_name",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceDeleteResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ask(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ask(
            question="question",
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ask_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ask(
            question="question",
            conversation_id="conversation_id",
            file_ids=["string"],
            file_names=["string"],
            output_schema={"foo": "bar"},
            reset=True,
            thinking_level="fast",
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ask(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.ask(
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ask(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.ask(
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceAskResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
            file_ids=["string"],
            file_names=["string"],
            thinking_level="fast",
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceExtractResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_file(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ingest_file(
            file=b"Example data",
        )
        assert_matches_type(SourceIngestFileResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_file_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ingest_file(
            file=b"Example data",
            partition_method="fast",
        )
        assert_matches_type(SourceIngestFileResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_file(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.ingest_file(
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceIngestFileResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_file(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.ingest_file(
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceIngestFileResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_github(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ingest_github(
            url="url",
        )
        assert_matches_type(SourceIngestGitHubResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_github(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.ingest_github(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceIngestGitHubResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_github(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.ingest_github(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceIngestGitHubResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_url(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ingest_url(
            url="url",
        )
        assert_matches_type(SourceIngestURLResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_url_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ingest_url(
            url="url",
            crawl_urls=True,
            partition_method="fast",
        )
        assert_matches_type(SourceIngestURLResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_url(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.ingest_url(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceIngestURLResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_url(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.ingest_url(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceIngestURLResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_youtube(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ingest_youtube(
            url="url",
        )
        assert_matches_type(SourceIngestYoutubeResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_youtube(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.ingest_youtube(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceIngestYoutubeResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_youtube(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.ingest_youtube(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceIngestYoutubeResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reprocess(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.reprocess(
            file_id="file_id",
        )
        assert_matches_type(SourceReprocessResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reprocess_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.reprocess(
            file_id="file_id",
            partition_method="fast",
        )
        assert_matches_type(SourceReprocessResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reprocess(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.reprocess(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceReprocessResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reprocess(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.reprocess(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceReprocessResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_chunks(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.retrieve_chunks(
            query="query",
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_chunks_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.retrieve_chunks(
            query="query",
            file_ids=["string"],
            file_names=["string"],
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_chunks(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.retrieve_chunks(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_chunks(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.retrieve_chunks(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True
