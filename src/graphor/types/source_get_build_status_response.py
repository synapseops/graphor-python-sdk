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
    Processing, Processing failed). When no history exists yet: not_found.
    """

    success: bool
    """True if the build completed successfully (status is Completed)."""

    created_at: Optional[str] = None
    """ISO8601 timestamp when the build (history) was created.

    Present when history exists.
    """

    elements: Optional[List[Element]] = None
    """Paginated list of parsed elements (chunks) for this build.

    Only present when suppress_elements=false and the build has completed (status
    Completed).
    """

    error: Optional[str] = None
    """Error message from the pipeline, if the build failed (e.g. processing_failed)."""

    file_id: Optional[str] = None
    """Source file identifier.

    Present when the build has been persisted (history exists).
    """

    file_name: Optional[str] = None
    """Display name of the source file. Present when the build has been persisted."""

    message: Optional[str] = None
    """Human-readable message (e.g. when status is not_found or processing)."""

    method: Optional[Method] = None
    """Public-facing partition method names for API v2.

    Maps to internal PartitionMethod as:

    - fast → basic
    - balanced → hi_res
    - accurate → hi_res_ft
    - vlm → mai
    - agentic → graphorlm
    """

    page: Optional[int] = None
    """Current page of elements (1-based).

    Null when no pagination was requested (all elements returned).
    """

    page_size: Optional[int] = None
    """Number of elements per page. Null when no pagination was requested."""

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
