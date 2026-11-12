from .._models import BaseModel

__all__ = ["SourceRenameFolderResponse"]


class SourceRenameFolderResponse(BaseModel):
    folder: str
    """The folder's former path"""

    moved: int
    """Sources moved"""

    new_folder: str
    """Its new path"""
