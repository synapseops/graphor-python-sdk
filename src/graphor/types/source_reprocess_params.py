# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .method import Method

__all__ = ["SourceReprocessParams"]


class SourceReprocessParams(TypedDict, total=False):
    file_id: Required[str]
    """Unique identifier of the source to re-process."""

    enrichment: Optional[str]
    """LLM enrichment level.

    `full` (default) runs page/section and document annotation; `none` returns
    parsing results only and is faster, at the cost of weaker retrieval context.
    """

    indexing: Optional[str]
    """Retrieval indexing level.

    `full` (default) chunks, embeds and indexes the source; `none` skips it — the
    source will NOT be searchable via ask/extract/retrieve, though its parsed
    elements remain readable. Reversible by re-processing.
    """

    method: Method
    """Partitioning strategy. One of: fast, balanced, accurate, agentic, auto."""
