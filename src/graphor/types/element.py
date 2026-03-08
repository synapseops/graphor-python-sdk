# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Element"]


class Element(BaseModel):
    """A single parsed element (chunk/partition) from a source, with explicit fields."""

    bounding_box: Optional[Dict[str, object]] = None
    """Bounding box (e.g. left, top, width, height) when available."""

    element_id: Optional[str] = None
    """Unique identifier for the element."""

    element_type: Optional[
        Literal[
            "Title",
            "NarrativeText",
            "TextBlock",
            "ListItem",
            "Table",
            "TableRow",
            "Image",
            "Footer",
            "Formula",
            "CompositeElement",
            "FigureCaption",
            "PageBreak",
            "Address",
            "EmailAddress",
            "PageNumber",
            "CodeSnippet",
            "Header",
            "FormKeysValues",
            "Link",
            "UncategorizedText",
            "Abstract",
            "AsideText",
            "Reference",
            "ReferenceContent",
            "Chart",
            "Seal",
            "FormulaNumber",
        ]
    ] = None
    """Type of the element (Title, NarrativeText, Image, Table, etc.)."""

    html: Optional[str] = None
    """HTML representation of the content, when available."""

    img_base64: Optional[str] = None
    """Base64-encoded image data, when the element is an image."""

    markdown: Optional[str] = None
    """Markdown representation of the content, when available."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata."""

    page_annotation: Optional[str] = None
    """Annotation/summary for the page containing this element."""

    page_keywords: Optional[List[str]] = None
    """Keywords extracted for the page."""

    page_layout: Optional[Dict[str, object]] = None
    """Page dimensions (width, height) when available."""

    page_number: Optional[int] = None
    """Page number (1-based) where the element appears."""

    page_topics: Optional[List[str]] = None
    """Topics extracted for the page."""

    position: Optional[int] = None
    """Order/position of the element within the document."""

    text: Optional[str] = None
    """Plain text content of the element."""
