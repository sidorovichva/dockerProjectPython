import pytest


@pytest.mark.parametrize("a, b, expect", [
    (1, 2, 3),
    (5, -3, 2),
    (3, -5, -2)
], ids=[
    "1 + 2 = 3",
    "5 + -3 = 2",
    "3 + -5 = -2"
])
def test_addition(a, b, expect):
    assert a + b == expect
