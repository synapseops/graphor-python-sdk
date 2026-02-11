# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["SourceAskResponse"]


class SourceAskResponse(BaseModel):
    answer: str
    """The answer to the question.

    When output_schema is provided, this will be a short status message and the
    structured data will be in structured_output (and the raw JSON-text in
    raw_json).
    """

    conversation_id: Optional[str] = None
    """Conversation identifier used to maintain memory context"""

    raw_json: Optional[str] = None
    """
    Optional raw JSON-text produced by the sources model before
    validation/correction.
    """

    structured_output: Optional[Dict[str, object]] = None
    """
    Optional structured output (object) validated against the requested
    output_schema.
    """
