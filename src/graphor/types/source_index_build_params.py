# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SourceIndexBuildParams"]


class SourceIndexBuildParams(TypedDict, total=False):
    file_id: Required[str]
    """Unique identifier of the source file."""

    build_id: Optional[str]
    """Build to index.

    Omitted → the file's active build. When given, that build becomes the active one
    (only the active build can serve retrieval).
    """
