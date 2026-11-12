from .._models import BaseModel

__all__ = ["SourceCreateFolderResponse"]


class SourceCreateFolderResponse(BaseModel):
    created: bool
    """False when the folder already existed"""

    folder: str
    """The folder's normalized path"""
