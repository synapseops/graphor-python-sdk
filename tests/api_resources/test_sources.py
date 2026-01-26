# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from graphor import Graphor, AsyncGraphor
from tests.utils import assert_matches_type
from graphor.types import (
    PublicSource,
    SourceAskResponse,
    SourceListResponse,
    SourceDeleteResponse,
    SourceExtractResponse,
    SourceLoadElementsResponse,
    SourceRetrieveChunksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Graphor) -> None:
        source = client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Graphor) -> None:
        source = client.sources.delete()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Graphor) -> None:
        source = client.sources.delete(
            file_id="file_id",
            file_name="file_name",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceDeleteResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_ask(self, client: Graphor) -> None:
        source = client.sources.ask(
            question="question",
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_ask_with_all_params(self, client: Graphor) -> None:
        source = client.sources.ask(
            question="question",
            conversation_id="conversation_id",
            file_ids=["string"],
            file_names=["string"],
            output_schema={"foo": "bar"},
            reset=True,
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_ask(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.ask(
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_extract(self, client: Graphor) -> None:
        source = client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: Graphor) -> None:
        source = client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
            file_ids=["string"],
            file_names=["string"],
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_load_elements(self, client: Graphor) -> None:
        source = client.sources.load_elements()
        assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_load_elements_with_all_params(self, client: Graphor) -> None:
        source = client.sources.load_elements(
            file_id="file_id",
            file_name="file_name",
            filter={
                "elements_to_remove": ["string"],
                "page_numbers": [0],
                "type": "type",
            },
            page=0,
            page_size=0,
        )
        assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_load_elements(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.load_elements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_load_elements(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.load_elements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_parse(self, client: Graphor) -> None:
        source = client.sources.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_parse_with_all_params(self, client: Graphor) -> None:
        source = client.sources.parse(
            file_id="file_id",
            file_name="file_name",
            partition_method="basic",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_parse(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_parse(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_chunks(self, client: Graphor) -> None:
        source = client.sources.retrieve_chunks(
            query="query",
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_chunks_with_all_params(self, client: Graphor) -> None:
        source = client.sources.retrieve_chunks(
            query="query",
            file_ids=["string"],
            file_names=["string"],
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_chunks(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.retrieve_chunks(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Graphor) -> None:
        source = client.sources.upload(
            file=b"raw file contents",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_github(self, client: Graphor) -> None:
        source = client.sources.upload_github(
            url="url",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_github(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.upload_github(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_github(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.upload_github(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_url(self, client: Graphor) -> None:
        source = client.sources.upload_url(
            url="url",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_url_with_all_params(self, client: Graphor) -> None:
        source = client.sources.upload_url(
            url="url",
            crawl_urls=True,
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_url(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.upload_url(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_url(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.upload_url(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_youtube(self, client: Graphor) -> None:
        source = client.sources.upload_youtube(
            url="url",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_youtube(self, client: Graphor) -> None:
        response = client.sources.with_raw_response.upload_youtube(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_youtube(self, client: Graphor) -> None:
        with client.sources.with_streaming_response.upload_youtube(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.delete()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.delete(
            file_id="file_id",
            file_name="file_name",
        )
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceDeleteResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceDeleteResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_ask(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ask(
            question="question",
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_ask_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.ask(
            question="question",
            conversation_id="conversation_id",
            file_ids=["string"],
            file_names=["string"],
            output_schema={"foo": "bar"},
            reset=True,
        )
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_ask(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.ask(
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceAskResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.extract(
            output_schema={"foo": "bar"},
            user_instruction="user_instruction",
            file_ids=["string"],
            file_names=["string"],
        )
        assert_matches_type(SourceExtractResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_load_elements(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.load_elements()
        assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_load_elements_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.load_elements(
            file_id="file_id",
            file_name="file_name",
            filter={
                "elements_to_remove": ["string"],
                "page_numbers": [0],
                "type": "type",
            },
            page=0,
            page_size=0,
        )
        assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_load_elements(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.load_elements()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_load_elements(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.load_elements() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceLoadElementsResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_parse(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_parse_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.parse(
            file_id="file_id",
            file_name="file_name",
            partition_method="basic",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.parse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.parse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_chunks(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.retrieve_chunks(
            query="query",
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_chunks_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.retrieve_chunks(
            query="query",
            file_ids=["string"],
            file_names=["string"],
        )
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_chunks(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.retrieve_chunks(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceRetrieveChunksResponse, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.upload(
            file=b"raw file contents",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_github(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.upload_github(
            url="url",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_github(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.upload_github(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_github(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.upload_github(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_url(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.upload_url(
            url="url",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_url_with_all_params(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.upload_url(
            url="url",
            crawl_urls=True,
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_url(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.upload_url(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_url(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.upload_url(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_youtube(self, async_client: AsyncGraphor) -> None:
        source = await async_client.sources.upload_youtube(
            url="url",
        )
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_youtube(self, async_client: AsyncGraphor) -> None:
        response = await async_client.sources.with_raw_response.upload_youtube(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(PublicSource, source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_youtube(self, async_client: AsyncGraphor) -> None:
        async with async_client.sources.with_streaming_response.upload_youtube(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(PublicSource, source, path=["response"])

        assert cast(Any, response.is_closed) is True
