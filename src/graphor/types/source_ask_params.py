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

    include_citation_images: Optional[bool]
    """
    When true, the response's `citations` entries are populated with a
    base64-encoded PNG screenshot of each cited page in `image_base64`. Increases
    payload size and latency — leave false (the default) when not needed and fetch
    screenshots on demand via
    `GET /sources/{file_id}/pages/{page_number}/screenshot`.
    """

    include_citation_markup: Optional[bool]
    """
    When true, the `answer` field keeps the structured citation markup
    `[N](file_id|pX|sY|eZ|fNAME)` emitted by the agent. When false (default), the
    markup is stripped to plain `[N]` markers and the structured data is exposed via
    `citations` instead. Note: the markup format is an implementation detail and may
    change in future versions — prefer the `citations` field for stable parsing. Has
    no effect when `output_schema` is set.
    """

    output_schema: Optional[Dict[str, object]]
    """Optional JSON Schema for requesting structured output.

    When provided, the answer field will contain a short status message and the
    structured data will be in structured_output.
    """

    reset: Optional[bool]
    """When true, starts a new conversation discarding any previous history"""

    thinking_level: Optional[Literal["fast", "balanced", "accurate", "max"]]
    """
    Controls model and thinking budget: 'fast' (cheapest/fastest), 'balanced',
    'accurate', or 'max' (most thorough)
    """
