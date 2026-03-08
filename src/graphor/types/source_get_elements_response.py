# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .element import Element
from .._models import BaseModel

__all__ = ["SourceGetElementsResponse"]


class SourceGetElementsResponse(BaseModel):
    items: List[Element]
    """List of items in the current page"""

    total: int
    """Total number of items"""

    page: Optional[int] = None
    """Current page"""

    page_size: Optional[int] = None
    """Items per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""
