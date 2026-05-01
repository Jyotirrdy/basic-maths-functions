import math

import maths_functions as mf


def test_arithmetic():
    assert mf.add(2, 3) == 5
    assert mf.subtract(5, 2) == 3
    assert mf.multiply(4, 3) == 12
    assert mf.divide(9, 3) == 3
    assert mf.modulus(10, 3) == 1


def test_advanced():
    assert mf.power(2, 4) == 16
    assert mf.square(6) == 36
    assert mf.cube(3) == 27
    assert mf.absolute(-8) == 8
    assert mf.average(2, 4, 6, 8) == 5
    assert mf.percentage(25, 200) == 12.5
    assert mf.factorial(5) == 120
    assert mf.is_even(12) is True
    assert mf.is_odd(7) is True
    assert math.isclose(mf.root(27, 3), 3)


def test_errors():
    try:
        mf.divide(1, 0)
        assert False
    except ZeroDivisionError:
        assert True

    try:
        mf.factorial(-1)
        assert False
    except ValueError:
        assert True
