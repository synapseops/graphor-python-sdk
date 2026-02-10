# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .public_partition_method import PublicPartitionMethod

__all__ = ["SourceUploadURLParams"]


class SourceUploadURLParams(TypedDict, total=False):
    url: Required[str]
    """The url of the source"""

    crawl_urls: Annotated[bool, PropertyInfo(alias="crawlUrls")]
    """Whether to crawl urls from the source"""

    partition_method: Optional[PublicPartitionMethod]
    """Partition methods available for public API endpoints."""
