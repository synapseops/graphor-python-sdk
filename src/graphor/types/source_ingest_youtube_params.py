# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SourceIngestYoutubeParams"]


class SourceIngestYoutubeParams(TypedDict, total=False):
    url: Required[str]
    """The YouTube video URL to ingest (e.g.

    https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    """

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

    folder: Optional[str]
    """Folder to store the source in, as a '/'-separated path (e.g. `Contracts/2026`).

    An empty string or '/' is the top level. A folder that does not exist is
    created. When omitted (or `None`), a new source goes to the top level and a
    source that replaces an existing one of the same name keeps that source's
    folder.
    """
