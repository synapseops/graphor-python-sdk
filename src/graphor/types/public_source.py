# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PublicSource"]


class PublicSource(BaseModel):
    file_name: str
    """Display name of the source file"""

    file_size: int
    """File size in bytes"""

    file_source: str
    """Origin of the file (e.g. local_file, url, github, youtube)"""

    file_type: str
    """File extension / type (e.g. pdf, docx, txt)"""

    message: str
    """Human-readable status message"""

    project_id: str
    """UUID of the project this source belongs to"""

    project_name: str
    """Display name of the project"""

    status: str
    """Current processing status of the source (e.g.

    completed, processing, failed, new)
    """

    file_id: Optional[str] = None
    """Unique identifier for the source"""

    method: Optional[str] = None
    """Partitioning strategy used during ingestion.

    V1 API: basic, hi_res, hi_res_ft, mai, graphorlm, auto. V2 API: fast, balanced,
    accurate, agentic, auto.
    """

    searchable: Optional[bool] = None
    """Whether this source has a retrieval index.

    False means it was ingested with indexing=none: `ask`, `extract` and `retrieve`
    will return nothing for it, while reading its elements, `grep` and page reads
    all still work. Null when unknown (pre-existing sources).
    """
