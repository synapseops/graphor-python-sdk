# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SourceIndexBuildResponse"]


class SourceIndexBuildResponse(BaseModel):
    """Response for ``POST /v2/sources/index``."""

    build_id: str
    """The build that was indexed."""

    chunks_indexed: int
    """Number of chunks embedded and stored for the build."""

    file_id: str
    """Unique identifier of the source file."""

    indexing: Optional[str] = None
    """Persisted indexing level after the operation (always 'full')."""

    success: Optional[bool] = None
    """Whether the operation succeeded."""
