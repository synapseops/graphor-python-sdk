# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceListParams"]


class SourceListParams(TypedDict, total=False):
    file_ids: Optional[SequenceNotStr[str]]
    """Optional list of file_id to filter by (only these sources are returned).

    Repeat the param for multiple IDs.
    """

    folder: str
    """Only the sources in this folder, a '/'-separated path, and (with `recursive`,
    the default) in the folders below it.

    An empty string or '/' lists only the sources at the top level.
    """

    recursive: bool
    """With `folder`, include the folders below it (the default).

    Without `folder`, `False` lists only the sources at the top level.
    """
