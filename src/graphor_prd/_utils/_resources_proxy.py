from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `graphor_prd.resources` module.

    This is used so that we can lazily import `graphor_prd.resources` only when
    needed *and* so that users can just import `graphor_prd` and reference `graphor_prd.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("graphor_prd.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
