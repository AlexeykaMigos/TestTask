import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    return TestClient(app)