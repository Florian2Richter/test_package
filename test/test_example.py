import pytest
from example_package_flo import example

@pytest.mark.parametrize(
    "value, expected",
    [
        (2, 3),
        (-1, 0)
    ]
)


def test_add_one(value, expected):
    ret = example.add_one(value)
    assert ret == expected