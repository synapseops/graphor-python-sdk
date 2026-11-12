from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceCreateFolderParams"]


class SourceCreateFolderParams(TypedDict, total=False):
    folder: Required[str]
    """The folder's path, '/'-separated (for example `Contracts/2026`).

    The folders above it are created too. Not the top level.
    """
