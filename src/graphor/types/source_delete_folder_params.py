from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceDeleteFolderParams"]


class SourceDeleteFolderParams(TypedDict, total=False):
    folder: Required[str]
    """The folder to delete"""
