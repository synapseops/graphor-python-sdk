from typing import List

from .._models import BaseModel

__all__ = ["SourceMoveResponse"]


class SourceMoveResponse(BaseModel):
    folder: str
    """The target folder; an empty string is the top level"""

    moved: int
    """Sources moved"""

    not_found: List[str]
    """Ids that matched no source of the project"""
