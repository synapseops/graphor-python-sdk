# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceRetrieveChunksParams"]


class SourceRetrieveChunksParams(TypedDict, total=False):
    query: Required[str]
    """The natural-language search query to find relevant chunks"""

    file_ids: Optional[SequenceNotStr[str]]
    """Optional list of file IDs to restrict retrieval scope (preferred)"""

    file_names: Optional[SequenceNotStr[str]]
    """
    Optional list of file names to restrict retrieval scope (deprecated, use
    file_ids)
    """
