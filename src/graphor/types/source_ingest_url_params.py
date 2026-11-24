# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .method import Method
from .._utils import PropertyInfo

__all__ = ["SourceIngestURLParams"]


class SourceIngestURLParams(TypedDict, total=False):
    url: Required[str]
    """The web page URL to ingest"""

    crawl_urls: Annotated[bool, PropertyInfo(alias="crawlUrls")]
    """When true, also follows and ingests links found on the page"""

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

    method: Optional[Method]
    """The processing method:

    - fast: heuristic parsing for clean text documents; transcription for audio, video and YouTube. The fastest.
    - balanced: OCR with a layout model; handles multi-column PDFs and mixed content.
    - accurate: fine-tuned models for forms, dense tables and specialized document types.
    - agentic: reads the page like a person; multi-page tables, diagrams and charts, with annotations for each image.
    - auto: classifies each page and runs the cheapest method that reads it correctly (PDF only).
    """

    folder: Optional[str]
    """Folder to store the source in, as a '/'-separated path (e.g. `Contracts/2026`).

    An empty string or '/' is the top level. A folder that does not exist is
    created. When omitted (or `None`), a new source goes to the top level and a
    source that replaces an existing one of the same name keeps that source's
    folder.
    """
