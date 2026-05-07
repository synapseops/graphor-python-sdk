# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceGetPageScreenshotParams"]


class SourceGetPageScreenshotParams(TypedDict, total=False):
    file_id: Required[str]

    max_width: int
    """Pixel width cap for the rendered image (clamped to 300-1600)."""
