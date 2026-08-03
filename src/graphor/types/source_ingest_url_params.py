# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .method import Method
from .._utils import PropertyInfo

__all__ = ["SourceIngestURLParams"]


class SourceIngestURLParams(TypedDict, total=False):
    url: Required[str]
    """The web page URL to ingest"""

    crawl_urls: Annotated[bool, PropertyInfo(alias="crawlUrls")]
    """When true, also follows and ingests links found on the page"""

    enrichment: Optional[str]
    """LLM enrichment level.

    `full` (default) runs page/section and document annotation; `none` returns
    parsing results only and is faster, at the cost of weaker retrieval context.
    """

    indexing: Optional[str]
    """Retrieval indexing level.

    `full` (default) chunks, embeds and indexes the source; `none` skips it — the
    source will NOT be searchable via ask/extract/retrieve, though its parsed
    elements remain readable. Reversible by re-processing.
    """

    method: Optional[Method]
    """Public-facing partition method names for API v2.

    Maps to internal PartitionMethod as:

    - fast → basic
    - balanced → hi_res
    - accurate → hi_res_ft
    - agentic → graphorlm
    - auto → auto
    """
