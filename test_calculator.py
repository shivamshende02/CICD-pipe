
from calculator import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 500


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_with_zero():
    assert add(5, 0) == 5


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_subtract_zero():
    assert subtract(5, 0) == 5
