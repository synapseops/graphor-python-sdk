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
    """Additional metadata for the chunk (e.g. element type, coordinates)"""

    page_number: Optional[int] = None
    """The page number where this chunk appears in the original document"""

    score: Optional[float] = None
    """Relevance score between 0 and 1 (higher is more relevant)"""


class SourceRetrieveChunksResponse(BaseModel):
    query: str
    """The original search query"""

    total: int
    """Total number of chunks retrieved"""

    chunks: Optional[List[Chunk]] = None
    """List of retrieved chunks ordered by relevance"""

    message: Optional[str] = None
    """Present only when the result needs explaining — e.g.

    every source in scope was ingested with indexing=none, so an empty chunk list
    means 'nothing is indexed', not 'nothing matched'.
    """
