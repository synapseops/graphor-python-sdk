# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceExtractParams"]


class SourceExtractParams(TypedDict, total=False):
    output_schema: Required[Dict[str, object]]
    """JSON Schema used to request a structured output.

    The system will extract data according to this schema.
    """

    user_instruction: Required[str]
    """User instruction to guide the extraction"""

    file_ids: Optional[SequenceNotStr[str]]
    """List of file IDs to extract from (preferred)"""

    file_names: Optional[SequenceNotStr[str]]
    """List of file names to extract from (deprecated, use file_ids)"""
