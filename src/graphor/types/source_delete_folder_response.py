from .._models import BaseModel

__all__ = ["SourceDeleteFolderResponse"]


class SourceDeleteFolderResponse(BaseModel):
    deleted: int
    """Folders removed: the folder and its empty subfolders"""

    folder: str
    """The deleted folder's path"""
