import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(0) == "E"  # edge case
    assert gauge(1) == "E"  # edge case (1% should return "E")
    assert gauge(50) == "50%"  # normal case
    assert gauge(99) == "F"  # edge case

def test_convert_invalid_format():
    # Test for invalid format (non-integer input)
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/4")

def test_convert_invalid_fraction():
    # Test for X > Y
    with pytest.raises(ValueError):
        convert("10/3")
    # Test for Y == 0
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
