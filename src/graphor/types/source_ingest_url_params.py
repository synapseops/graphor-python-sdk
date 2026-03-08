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

    partition_method: Optional[Method]
    """Public-facing partition method names for API v2.

    Maps to internal PartitionMethod as:

    - fast → basic
    - balanced → hi_res
    - accurate → hi_res_ft
    - vlm → mai
    - agentic → graphorlm
    """
