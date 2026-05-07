# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SourceGetPageScreenshotResponse"]


class SourceGetPageScreenshotResponse(BaseModel):
    """Base64-encoded PNG screenshot of a page from a source file."""

    file_id: str
    """The unique identifier of the source file."""

    image_base64: str
    """Base64-encoded PNG image bytes."""

    page_number: int
    """1-based page number that was rendered."""

    file_name: Optional[str] = None
    """Display name of the source file."""

    height: Optional[int] = None
    """Pixel height of the rendered image."""

    mime_type: Optional[str] = None
    """MIME type of the encoded image (always image/png)."""

    width: Optional[int] = None
    """Pixel width of the rendered image."""
