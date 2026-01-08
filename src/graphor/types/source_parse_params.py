# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .partition_method import PartitionMethod

__all__ = ["SourceParseParams"]


class SourceParseParams(TypedDict, total=False):
    file_name: Required[str]
    """The name of the file"""

    partition_method: PartitionMethod
    """The method used to partition the file"""
