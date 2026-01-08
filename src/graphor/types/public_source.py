# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .partition_method import PartitionMethod

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

    partition_method: Optional[PartitionMethod] = None
