from __future__ import annotations

from pydantic import Field
from pydantic_zarr.v2 import ArraySpec, GroupSpec

from ome_zarr_models.base import BaseAttrs
from ome_zarr_models.v04.base import BaseGroupv04

__all__ = ["Labels", "LabelsAttrs"]


class LabelsAttrs(BaseAttrs):
    """
    Attributes for an OME-Zarr labels dataset.
    """

    labels: list[str] = Field(
        ..., description="List of paths to labels arrays within a labels dataset."
    )


class Labels(GroupSpec[LabelsAttrs, ArraySpec | GroupSpec], BaseGroupv04):  # type: ignore[misc]
    """
    An OME-Zarr labels dataset.
    """
