from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceRemoveFolderParams"]


class SourceRemoveFolderParams(TypedDict, total=False):
    folder: Required[str]
    """The folder to remove"""

    merge: bool
    """
    Merge a subfolder into a folder of the same name above it, instead of answering
    409 `folder.exists`
    """
