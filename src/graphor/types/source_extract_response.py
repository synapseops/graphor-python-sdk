# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["SourceExtractResponse"]


class SourceExtractResponse(BaseModel):
    file_names: List[str]
    """List of file names used for extraction"""

    file_ids: Optional[List[str]] = None
    """List of file IDs used for extraction"""

    raw_json: Optional[str] = None
    """Raw JSON-text produced by the model before validation/correction."""

    structured_output: Optional[Dict[str, object]] = None
    """Structured output (object) matching the requested output_schema."""
