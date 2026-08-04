# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .method import Method
from .._types import FileTypes

__all__ = ["SourceIngestFileParams"]


class SourceIngestFileParams(TypedDict, total=False):
    file: Required[FileTypes]

    enrichment: Optional[str]
    """
    LLM enrichment level: 'full' (default) or 'none' to skip page/section/document
    annotation for faster parsing.
    """

    indexing: Optional[str]
    """
    Retrieval indexing level: 'full' (default) or 'none' to skip
    chunking/embedding/indexing — the source is parsed but not searchable. Requires
    Temporal ingestion.
    """

    method: Optional[Method]
    """Public-facing partition method names for API v2.

    Maps to internal PartitionMethod as:

    - fast → basic
    - balanced → hi_res
    - accurate → hi_res_ft
    - agentic → graphorlm
    - auto → auto
    """
