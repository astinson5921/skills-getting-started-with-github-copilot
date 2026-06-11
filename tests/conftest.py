import copy
import pytest
from fastapi.testclient import TestClient
import src.app as appmodule


_initial_activities = copy.deepcopy(appmodule.activities)


@pytest.fixture
def client():
    with TestClient(appmodule.app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    # Reset the in-memory activities before each test to avoid cross-test pollution
    appmodule.activities = copy.deepcopy(_initial_activities)
