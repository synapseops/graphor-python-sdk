# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SourceDeleteResponse"]


class SourceDeleteResponse(BaseModel):
    file_name: str
    """The name of the deleted file"""

    message: str
    """The message of the deletion"""

    project_id: str
    """The ID of the project"""

    project_name: str
    """The name of the project"""

    status: str
    """The status of the deletion"""
