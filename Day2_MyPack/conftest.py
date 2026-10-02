import pytest


@pytest.fixture()
def setup():
    print("setup environment fixture")
    yield
    print("teardown environment fixture")