# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceExtractParams"]


class SourceExtractParams(TypedDict, total=False):
    file_names: Required[SequenceNotStr[str]]
    """List of file names to extract from"""

    output_schema: Required[Dict[str, object]]
    """JSON Schema used to request a structured output.

    The system will extract data according to this schema.
    """

    user_instruction: Required[str]
    """User instruction to guide the extraction"""
