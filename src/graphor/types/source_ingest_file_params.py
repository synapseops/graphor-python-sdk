# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .method import Method
from .._types import FileTypes

__all__ = ["SourceIngestFileParams"]


class SourceIngestFileParams(TypedDict, total=False):
    file: Required[FileTypes]

    folder: str
    """Folder to store the source in, as a '/'-separated path (e.g. `Contracts/2026`).

    An empty string, '/' or omitted is the top level. A folder that does not exist
    is created.
    """

    enrichment: Optional[str]
    """
    LLM enrichment level: 'full' (default) or 'none' to skip page/section/document
    annotation for faster parsing.
    """

    indexing: Optional[str]
    """
    Retrieval indexing level: 'full' (default) or 'none' to skip
    chunking/embedding/indexing — the source is parsed but not searchable.
    """

    method: Optional[Method]
    """The processing method:

    - fast: heuristic parsing for clean text documents; transcription for audio, video and YouTube. The fastest.
    - balanced: OCR with a layout model; handles multi-column PDFs and mixed content.
    - accurate: fine-tuned models for forms, dense tables and specialized document types.
    - agentic: reads the page like a person; multi-page tables, diagrams and charts, with annotations for each image.
    - auto: classifies each page and runs the cheapest method that reads it correctly (PDF only).
    """
