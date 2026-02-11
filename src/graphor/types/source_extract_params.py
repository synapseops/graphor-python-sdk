# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceExtractParams"]


class SourceExtractParams(TypedDict, total=False):
    output_schema: Required[Dict[str, object]]
    """JSON Schema describing the desired structured output shape.

    The model will produce data conforming to this schema.
    """

    user_instruction: Required[str]
    """Natural-language instruction guiding what information to extract"""

    file_ids: Optional[SequenceNotStr[str]]
    """List of file IDs to extract from (preferred)"""

    file_names: Optional[SequenceNotStr[str]]
    """List of file names to extract from (deprecated, use file_ids)"""

    thinking_level: Optional[Literal["fast", "balanced", "accurate"]]
    """
    Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced', or
    'accurate' (most thorough)
    """
