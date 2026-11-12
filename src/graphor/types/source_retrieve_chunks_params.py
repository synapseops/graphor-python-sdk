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

    folders: Optional[SequenceNotStr[str]]
    """
    Folders to restrict the scope to (at most 1,000): every source at or below each
    folder, read when the request arrives, together with any `file_ids`. A folder is
    a '/'-separated path. An empty list is no folder scope. A folder that holds no
    source refuses the request (400 `chat.folder_scope_empty`); the top level, an
    invalid path, or `folders` together with `file_names` answers 422
    `request.invalid`.
    """
