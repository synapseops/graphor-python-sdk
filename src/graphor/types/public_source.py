# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PublicSource"]


class PublicSource(BaseModel):
    file_name: str

    file_size: int

    file_source: str

    file_type: str

    message: str

    project_id: str

    project_name: str

    status: str

    file_id: Optional[str] = None
    """Unique identifier for the source"""

    partition_method: Optional[
        Literal["basic", "hi_res", "hi_res_ft", "mai", "graphorlm", "ocr", "advanced", "yolox"]
    ] = None
