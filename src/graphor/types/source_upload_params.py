# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["SourceUploadParams"]


class SourceUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    partition_method: Optional[Literal["basic", "hi_res", "hi_res_ft", "mai", "graphorlm"]]
    """Partition methods available for public API endpoints."""
