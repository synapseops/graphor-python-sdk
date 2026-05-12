# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .method import Method

__all__ = ["SourceReprocessParams"]


class SourceReprocessParams(TypedDict, total=False):
    file_id: Required[str]
    """Unique identifier of the source to re-process."""

    method: Method
    """Partitioning strategy. One of: fast, balanced, accurate, agentic, auto."""
