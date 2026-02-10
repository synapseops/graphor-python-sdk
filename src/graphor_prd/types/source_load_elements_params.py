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
    """The filter of the elements"""

    page: Optional[int]
    """Current page number"""

    page_size: Optional[int]
    """Number of items per page"""


class Filter(TypedDict, total=False):
    """The filter of the elements"""

    elements_to_remove: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="elementsToRemove")]
    """The elements to remove"""

    page_numbers: Optional[Iterable[int]]
    """The page numbers of the elements"""

    type: Optional[str]
    """The type of the element"""
