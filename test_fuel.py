from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):
        convert("100 / 0")
    with pytest.raises(ValueError):
        convert("100 / 3")
    with pytest.raises(ValueError):
        convert("three/four")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
