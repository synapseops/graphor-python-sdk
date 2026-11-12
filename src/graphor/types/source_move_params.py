from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceMoveParams"]


class SourceMoveParams(TypedDict, total=False):
    file_ids: Required[SequenceNotStr[str]]
    """The sources to move (1 to 1,000)"""

    folder: Required[str]
    """The target folder, '/'-separated; an empty string or '/' is the top level.

    A folder that does not exist is created.
    """
