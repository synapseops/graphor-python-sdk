# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SourceGetBuildStatusParams"]


class SourceGetBuildStatusParams(TypedDict, total=False):
    page: Optional[int]

    page_size: Optional[int]

    suppress_elements: bool

    suppress_img_base64: bool
