from fuel import gauge,convert
import pytest

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert convert("0/1") == 0

def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert convert("1/1") == 100
    assert convert("99/100") == 99

def test_half():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

def test_str():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
