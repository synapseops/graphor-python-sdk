# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SourceUploadURLParams"]


class SourceUploadURLParams(TypedDict, total=False):
    url: Required[str]
    """The url of the source"""

    crawl_urls: Annotated[bool, PropertyInfo(alias="crawlUrls")]
    """Whether to crawl urls from the source"""

    partition_method: Optional[Literal["basic", "hi_res", "hi_res_ft", "mai", "graphorlm"]]
    """Partition methods available for public API endpoints."""
