from calculator import add, sub, multiply, power
import pytest

from calculator import add, sub, root
    from calculator import add, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_root_square():
    assert root(2, 9) == pytest.approx(3.0)


def test_root_cube():
    assert root(3, 27) == pytest.approx(3.0)


def test_root_index_zero_raises():
    with pytest.raises(ValueError):
        root(0, 9)


def test_root_negative_even_index_raises():
    with pytest.raises(ValueError):
        root(2, -4)


def test_root_negative_odd_index():
    assert root(3, -8) == pytest.approx(-2.0)
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(7, 1) == 7
    assert power(2, -2) == 0.25
