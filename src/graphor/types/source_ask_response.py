# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["SourceAskResponse", "Citation", "Usage"]


class Citation(BaseModel):
    """A structured citation extracted from the inline ``[N]`` markers in the answer.

    Each citation corresponds to one ``[N]`` marker in the ``answer`` text.  Use
    the ``index`` field to map between the marker and the citation entry.
    """

    element_id: Optional[str] = None
    """Optional element identifier within the page/section (e.g.

    a specific paragraph or table).
    """

    file_id: Optional[str] = None
    """The unique identifier of the source file the citation refers to."""

    file_name: Optional[str] = None
    """Display name of the source file."""

    image_base64: Optional[str] = None
    """Base64-encoded PNG screenshot of the cited page.

    Only populated when the request was made with `include_citation_images=true`.
    May be null if the underlying source is not visualizable (e.g. plain text).
    """

    index: Optional[int] = None
    """The 1-based citation number that appears as `[N]` in the answer text."""

    page_number: Optional[int] = None
    """1-based page number where the cited content appears."""

    section_number: Optional[int] = None
    """Optional section number within the page."""

    text_preview: Optional[str] = None
    """Short text excerpt around the cited content, useful for quick context."""


class Usage(BaseModel):
    """Token usage breakdown for this request."""

    cache_read_tokens: Optional[int] = None

    cache_write_tokens: Optional[int] = None

    om_tokens_in: Optional[int] = None

    om_tokens_out: Optional[int] = None

    tokens_in: Optional[int] = None

    tokens_out: Optional[int] = None


class SourceAskResponse(BaseModel):
    answer: str
    """The answer to the question.

    When output_schema is provided, this will be a short status message and the
    structured data will be in structured_output (and the raw JSON-text in
    raw_json). Inline citations appear as `[N]` markers; use the `citations` field
    to resolve each marker to its source.
    """

    citations: Optional[List[Citation]] = None
    """Structured citations extracted from the `[N]` markers in `answer`.

    When the request includes `include_citation_images=true`, each entry carries a
    base64-encoded PNG screenshot of the cited page in `image_base64`.
    """

    conversation_id: Optional[str] = None
    """Conversation identifier used to maintain memory context"""

    elapsed_s: Optional[float] = None
    """Wall-clock time in seconds for the request."""

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

    usage: Optional[Usage] = None
    """Token usage breakdown for this request."""
