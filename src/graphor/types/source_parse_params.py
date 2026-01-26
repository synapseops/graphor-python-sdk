# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .partition_method import PartitionMethod

__all__ = ["SourceParseParams"]


class SourceParseParams(TypedDict, total=False):
    file_id: Optional[str]
    """Unique identifier for the source (preferred)"""

    file_name: Optional[str]
    """The name of the file (deprecated, use file_id)"""

    partition_method: PartitionMethod
    """The method used to partition the file"""
