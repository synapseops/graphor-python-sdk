# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SourceDeleteResponse"]


class SourceDeleteResponse(BaseModel):
    file_name: str
    """Display name of the deleted file"""

    message: str
    """Human-readable result message"""

    project_id: str
    """UUID of the project"""

    project_name: str
    """Display name of the project"""

    status: str
    """Result status of the deletion (e.g. 'success')"""

    file_id: Optional[str] = None
    """Unique identifier of the deleted source"""
