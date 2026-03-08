# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SourceIngestYoutubeResponse"]


class SourceIngestYoutubeResponse(BaseModel):
    build_id: str
    """The ID of the build. This ID can be used to check the status of the request."""

    error: Optional[str] = None
    """If the request was not successful, this will contain an error message."""

    success: Optional[bool] = None
    """Whether the request was successfully scheduled."""
