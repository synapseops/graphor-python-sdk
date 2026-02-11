# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceAskParams"]


class SourceAskParams(TypedDict, total=False):
    question: Required[str]
    """The natural-language question to ask about the sources"""

    conversation_id: Optional[str]
    """Conversation identifier to maintain memory context across multiple turns"""

    file_ids: Optional[SequenceNotStr[str]]
    """Optional list of file IDs to restrict search scope (preferred)"""

    file_names: Optional[SequenceNotStr[str]]
    """
    Optional list of file display names to restrict search scope (deprecated, use
    file_ids)
    """

    output_schema: Optional[Dict[str, object]]
    """Optional JSON Schema for requesting structured output.

    When provided, the answer field will contain a short status message and the
    structured data will be in structured_output.
    """

    reset: Optional[bool]
    """When true, starts a new conversation discarding any previous history"""

    thinking_level: Optional[Literal["fast", "balanced", "accurate"]]
    """
    Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced', or
    'accurate' (most thorough)
    """
