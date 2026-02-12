# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes
from .public_partition_method import PublicPartitionMethod

__all__ = ["SourceUploadParams"]


class SourceUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    partition_method: Optional[PublicPartitionMethod]
    """Partition methods available for public API endpoints.

    Each value also has a human-readable alias:

    - `basic` → **Fast**
    - `hi_res` → **Balanced**
    - `hi_res_ft` → **Accurate**
    - `mai` → **VLM**
    - `graphorlm` → **Agentic**
    """
