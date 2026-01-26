# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["SourceRetrieveChunksResponse", "Chunk"]


class Chunk(BaseModel):
    text: str
    """The text content of the chunk"""

    file_id: Optional[str] = None
    """The unique identifier of the source file"""

    file_name: Optional[str] = None
    """The source file name"""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata for the chunk"""

    page_number: Optional[int] = None
    """The page number of the chunk"""

    score: Optional[float] = None
    """The relevance score of the chunk"""


class SourceRetrieveChunksResponse(BaseModel):
    query: str
    """The original search query"""

    total: int
    """Total number of chunks retrieved"""

    chunks: Optional[List[Chunk]] = None
    """List of retrieved chunks"""
