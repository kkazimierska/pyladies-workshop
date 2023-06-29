def test_always_passes():
    assert True

# def test_always_fails():
#     assert False

def test_uppercase():
    assert "loud noises".replace(" ", "-") == "loud-noises"

import pytest

@pytest.fixture
def example_fixture_tekst():
    return "Dzis jest pieknie"

def test_with_fixture(example_fixture_tekst):
    assert example_fixture_tekst.count()  == 20