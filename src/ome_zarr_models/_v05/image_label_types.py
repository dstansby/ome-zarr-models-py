from typing import Literal

from ome_zarr_models.v04.image_label_types import (
    RGBA,
    Color,
    LabelBase,
    Property,
    Source,
    Uint8,
)

__all__ = [
    "RGBA",
    "Color",
    "Property",
    "Source",
    "Uint8",
]


class Label(LabelBase):
    """
    Metadata for a single image-label.
    """

    version: Literal["0.5"] | None = None