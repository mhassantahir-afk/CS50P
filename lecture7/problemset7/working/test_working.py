from working import convert
import pytest

def test_1():
    assert convert("5 AM to 6 PM") == "05:00 to 18:00"

def test_2():
    with pytest.raises(ValueError):
        convert("lkdcjsandcl")

def test_3():
    assert convert("5:00 PM to 6:00 AM") == "17:00 to 06:00"

def test_4():
    with pytest.raises(ValueError):
        convert("17:00 AM to 15:00 PM")
