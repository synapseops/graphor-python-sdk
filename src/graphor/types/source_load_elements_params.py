# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SourceLoadElementsParams", "Filter"]


class SourceLoadElementsParams(TypedDict, total=False):
    file_id: Optional[str]
    """Unique identifier for the source (preferred)"""

    file_name: Optional[str]
    """The name of the file (deprecated, use file_id)"""

    filter: Optional[Filter]
    """Optional filter to narrow down the returned elements"""

    page: Optional[int]
    """Current page number"""

    page_size: Optional[int]
    """Number of items per page"""


class Filter(TypedDict, total=False):
    """Optional filter to narrow down the returned elements"""

    elements_to_remove: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="elementsToRemove")]
    """List of element types to exclude from the results"""

    page_numbers: Optional[Iterable[int]]
    """Restrict results to specific page numbers from the original document"""

    type: Optional[str]
    """Filter by element type (e.g. NarrativeText, Title, Table)"""
