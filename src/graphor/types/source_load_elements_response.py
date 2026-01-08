# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourceLoadElementsResponse", "Item"]


class Item(BaseModel):
    """Class for storing a piece of text and associated metadata.

    Example:

        .. code-block:: python

            from langchain_core.documents import Document

            document = Document(page_content="Hello, world!", metadata={"source": "https://example.com"})
    """

    page_content: str

    id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    type: Optional[Literal["Document"]] = None


class SourceLoadElementsResponse(BaseModel):
    items: List[Item]
    """List of items in the current page"""

    total: int
    """Total number of items"""

    page: Optional[int] = None
    """Current page"""

    page_size: Optional[int] = None
    """Items per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""
