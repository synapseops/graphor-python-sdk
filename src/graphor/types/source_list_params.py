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
