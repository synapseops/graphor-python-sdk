# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .method import Method
from .element import Element
from .._models import BaseModel

__all__ = ["SourceGetBuildStatusResponse"]


class SourceGetBuildStatusResponse(BaseModel):
    """
    Status and optional result for an async build (ingestion/re-process) identified by build_id.

    Returned by GET /v2/sources/builds/{build_id}. When the build has completed successfully,
    includes file_id, file_name, and optionally paginated elements (parsed chunks).
    """

    build_id: str
    """The build identifier returned when the ingestion was scheduled."""

    status: str
    """Current build status.

    When a build history exists, this is a SourceNodeStatus value (e.g. Completed,
    Completed with errors, Processing, Processing failed). When no history exists
    yet: not_found.
    """

    success: bool
    """True if the build completed (status is Completed or Completed with errors)."""

    created_at: Optional[str] = None
    """ISO8601 timestamp when the build (history) was created.

    Present when history exists.
    """

    document_annotation: Optional[str] = None
    """Document-level summary/annotation from the build history.

    Present when history exists.
    """

    elements: Optional[List[Element]] = None
    """Paginated list of parsed elements (chunks) for this build.

    Only present when suppress_elements=false and the build has completed (status
    Completed or Completed with errors).
    """

    enrichment: Optional[str] = None
    """LLM enrichment level used for this build."""

    error: Optional[str] = None
    """Error message from the pipeline, if the build failed (e.g. processing_failed)."""

    error_code: Optional[str] = None
    """A machine-readable code for the failure, when there is one.

    For example `ingestion.invalid_link`, `ingestion.provider_unavailable` or
    `ingestion.method_unavailable`. Match on it rather than on the text of `error`;
    see the error codes in the API docs.
    """

    failed_batches_count: Optional[int] = None
    """Number of failed batches when status is 'Completed with errors'.

    Null otherwise.
    """

    file_id: Optional[str] = None
    """Source file identifier.

    Present when the build has been persisted (history exists).
    """

    file_name: Optional[str] = None
    """Display name of the source file. Present when the build has been persisted."""

    has_failed_batches: Optional[bool] = None
    """True when the build has failed batch details available for retry."""

    indexing: Optional[str] = None
    """Retrieval indexing level used for this build."""

    message: Optional[str] = None
    """Human-readable message (e.g. when status is not_found or processing)."""

    method: Optional[Method] = None
    """The processing method:

    - fast: heuristic parsing for clean text documents; transcription for audio, video and YouTube. The fastest.
    - balanced: OCR with a layout model; handles multi-column PDFs and mixed content.
    - accurate: fine-tuned models for forms, dense tables and specialized document types.
    - agentic: reads the page like a person; multi-page tables, diagrams and charts, with annotations for each image.
    - auto: classifies each page and runs the cheapest method that reads it correctly (PDF only).
    """

    page: Optional[int] = None
    """Current page of elements (1-based).

    Null when no pagination was requested (all elements returned).
    """

    page_size: Optional[int] = None
    """Number of elements per page. Null when no pagination was requested."""

    searchable: Optional[bool] = None
    """
    Whether this build's retrieval index is currently serving queries: the build
    completed, was indexed (indexing=full), and is still the source's active build.
    False for unindexed, failed, in-progress, or superseded builds: ask, extract and
    retrieve do not use them (for a superseded build they use the source's newer
    active build).
    """

    total_elements: Optional[int] = None
    """Total number of elements for this build. Present when suppress_elements=false."""

    total_pages: Optional[int] = None
    """Total pages in the source for this build. Present when history exists."""

    total_pages_elements: Optional[int] = None
    """Total number of pages of elements. Null when no pagination was requested."""

    total_partitions: Optional[int] = None
    """Total number of partitions created in this build. Present when history exists."""

    updated_at: Optional[str] = None
    """ISO8601 timestamp when the build (history) was last updated.

    Present when history exists.
    """
