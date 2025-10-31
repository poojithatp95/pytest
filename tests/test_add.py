from myproj import add
import pytest


def test_add_positive():
    """Test addition of positive integers."""
    assert add(1, 2) == 3


def test_add_negative():
    """Test addition of negative integers."""
    assert add(-1, -1) == -2


def test_add_zero():
    """Test addition with zero."""
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_floating_point():
    """Test addition of floating point numbers."""
    assert pytest.approx(add(0.1, 0.2)) == 0.3
    assert pytest.approx(add(1.5, 2.5)) == 4.0


def test_add_large_numbers():
    """Test addition of large integers."""
    assert add(1000000, 2000000) == 3000000
    assert add(999999999, 1) == 1000000000


def test_add_mixed_signs():
    """Test addition of positive and negative numbers."""
    assert add(-10, 15) == 5
    assert add(10, -15) == -5
    assert add(-10, -15) == -25


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (1000, -1000, 0),
    (42, -42, 0),
])
def test_add_parametrized(a: int, b: int, expected: int):
    """Parametrized test for multiple add scenarios."""
    assert add(a, b) == expected
