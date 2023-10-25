import pytest


@pytest.mark.regression
def test_numbers():
    assert 1 + 1 == 2
