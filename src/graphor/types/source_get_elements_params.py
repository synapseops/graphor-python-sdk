# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SourceGetElementsParams"]


class SourceGetElementsParams(TypedDict, total=False):
    file_id: Required[str]
    """Unique identifier of the source"""

    element_ids: Optional[SequenceNotStr[str]]
    """Restrict to specific element IDs (repeat param for multiple)"""

    elements_to_remove: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="elementsToRemove")]
    """Element types to exclude"""

    page: Optional[int]
    """1-based page number (use with page_size)"""

    page_numbers: Optional[Iterable[int]]
    """Restrict to specific page numbers"""

    page_size: Optional[int]
    """Number of elements per page"""

    suppress_img_base64: bool
    """When true, img_base64 is omitted from each element"""

    type: Optional[str]
    """Filter by element type (e.g. NarrativeText, Title)"""
