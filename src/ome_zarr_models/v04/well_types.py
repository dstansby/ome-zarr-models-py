"""
For reference, see the [well section of the OME-zarr specification](https://ngff.openmicroscopy.org/0.4/#well-md).
"""

from collections import defaultdict
from typing import Annotated, Literal

from pydantic import AfterValidator, Field

from ome_zarr_models._utils import _AlphaNumericConstraint, _unique_items_validator
from ome_zarr_models.base import BaseAttrs

# WellGroup is defined one level higher
__all__ = ["WellImage", "WellMeta"]


class WellImage(BaseAttrs):
    """
    A single image within a well.
    """

    path: Annotated[str, _AlphaNumericConstraint]
    acquisition: int | None = Field(
        None, description="A unique identifier within the context of the plate"
    )


class WellMeta(BaseAttrs):
    """
    Metadata for a single well.
    """

    images: Annotated[list[WellImage], AfterValidator(_unique_items_validator)]
    version: Literal["0.4"] | None = Field(
        None, description="Version of the well specification"
    )

    def get_acquisition_paths(self) -> dict[int, list[str]]:
        """
        Get mapping from acquisition indices to corresponding paths.

        Returns
        -------
        dict
            Dictionary with `(acquisition index: [image_path])` key/value
            pairs.

        Raises
        ------
        ValueError
            If an element of `self.well.images` has no `acquisition` attribute.
        """
        acquisition_dict: dict[int, list[str]] = defaultdict(list)
        for image in self.images:
            if image.acquisition is None:
                raise ValueError(
                    "Cannot get acquisition paths for Zarr files without "
                    "'acquisition' metadata at the well level"
                )
            acquisition_dict[image.acquisition].append(image.path)
        return dict(acquisition_dict)
