from pydantic_zarr.v3 import AnyArraySpec, ArraySpec, NamedConfig

from ome_zarr_models._v06 import Image
from ome_zarr_models._v06.coordinate_transforms import (
    TRANSFORM_REGISTRY,
    Axis,
    CoordinateSystem,
    Point,
    _TransformRegistry,
    Scale,
)

array_specs: list[AnyArraySpec] = [
    ArraySpec(
        shape=(100, 100),
        data_type="uint16",
        chunk_grid=NamedConfig(
            name="regular",
            configuration={"chunk_shape": [32, 32]},
        ),
        chunk_key_encoding=NamedConfig(
            name="default", configuration={"separator": "/"}
        ),
        fill_value=0,
        codecs=[NamedConfig(name="bytes")],
        dimension_names=["y", "x"],
    ),
    ArraySpec(
        shape=(50, 50),
        data_type="uint16",
        chunk_grid=NamedConfig(
            name="regular",
            configuration={"chunk_shape": [32, 32]},
        ),
        chunk_key_encoding=NamedConfig(
            name="default", configuration={"separator": "/"}
        ),
        fill_value=0,
        codecs=[NamedConfig(name="bytes")],
        dimension_names=["y", "x"],
    ),
]

image = Image.new(
    array_specs=array_specs,
    paths=["0", "1"],
    scales=[[1, 1], [2, 2]],
    translations=[None, None],
    name="my_image",
    output_coord_transform=Scale(
        scale=(
            0.5,
            0.2,
        )
    ),
    output_coord_system=CoordinateSystem(
        name="my_image_coords",
        axes=(
            Axis(name="y", type="space", unit="micrometer"),
            Axis(name="x", type="space", unit="micrometer"),
        ),
    ),
)

array_coord = Point(
    coordinates={"y": 1, "x": 2},
    coordinate_system=image.datasets[0][0].array_coordinate_system_name,
)

from rich import print

print(TRANSFORM_REGISTRY._graph)
print(array_coord)
print(array_coord.transform_to("my_image_coords"))
