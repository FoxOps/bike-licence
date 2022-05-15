from bl_functions import time_passed


def test_time_passed():
    assert time_passed('02/01/1991') == 31
