from typing import List

from .._models import BaseModel

__all__ = ["SourceListFoldersResponse", "Folder"]


class Folder(BaseModel):
    folder: str
    """The folder's path, '/'-separated"""


class SourceListFoldersResponse(BaseModel):
    folders: List[Folder]
    """Every folder of the project, with the folders above them, sorted.

    Folders created empty, folders that hold sources and folders uploads are on
    their way to.
    """

    truncated: bool
    """True when the project has more folders than this answer lists (at most 10,000)"""
