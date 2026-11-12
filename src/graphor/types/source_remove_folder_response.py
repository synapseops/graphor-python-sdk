from .._models import BaseModel

__all__ = ["SourceRemoveFolderResponse"]


class SourceRemoveFolderResponse(BaseModel):
    folder: str
    """The removed folder's path"""

    moved: int
    """Sources moved"""

    parent: str
    """Where its content went; an empty string is the top level"""
