from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceRenameFolderParams"]


class SourceRenameFolderParams(TypedDict, total=False):
    folder: Required[str]
    """The folder to rename"""

    new_folder: Required[str]
    """Its new path; it may sit under another folder"""

    merge: bool
    """
    Merge into `new_folder` when it already exists, instead of answering 409
    `folder.exists`
    """
