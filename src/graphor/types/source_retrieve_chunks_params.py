# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceRetrieveChunksParams"]


class SourceRetrieveChunksParams(TypedDict, total=False):
    query: Required[str]
    """The search query to retrieve relevant chunks"""

    file_names: Optional[SequenceNotStr[str]]
    """Optional list of file names to restrict retrieval to one or more documents"""
