# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SourceAskParams"]


class SourceAskParams(TypedDict, total=False):
    question: Required[str]
    """The question to ask about the sources"""

    conversation_id: Optional[str]
    """Conversation identifier to maintain memory context"""

    file_names: Optional[SequenceNotStr[str]]
    """Optional list of file display names to restrict search to one or more documents"""

    output_schema: Optional[Dict[str, object]]
    """Optional JSON Schema used to request a structured output.

    When provided, the system will first ask the sources model to output JSON-text,
    then validate/correct it with gemini-3-flash-preview.
    """

    reset: Optional[bool]
    """When true, starts a new conversation and ignores history"""
