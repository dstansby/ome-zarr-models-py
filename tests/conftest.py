import pytest
from zarr import MemoryStore


@pytest.fixture
def store(request: pytest.FixtureRequest) -> MemoryStore:
    match request.param:
        case "memory":
            return MemoryStore()
        case _:
            raise ValueError(f"Invalid store requested: {request.param}")
