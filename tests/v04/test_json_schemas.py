import json
from pathlib import Path

import zarr
from hypothesis import HealthCheck, assume, given, settings
from hypothesis_jsonschema import from_schema

from ome_zarr_models.v04.well import Well


def load_schema(fname: str):
    with (Path(__file__).parent / "data" / "schemas" / fname).open() as f:
        return json.load(f)


def test_json(attributes, ome_zarr_group):
    group = zarr.create_group(store={}, attributes=attributes)
    ome_zarr_group.from_zarr(group)


@settings(suppress_health_check=[HealthCheck.filter_too_much])
@given(from_schema(load_schema("well.schema")))
def test_well_schema(well_json):
    assume("well" in well_json)
    test_json(well_json, Well)
