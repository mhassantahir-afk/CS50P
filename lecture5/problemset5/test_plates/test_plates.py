from plates import is_valid

def test_cs50():
    assert is_valid("cs50") == True

def test_cs50p():
    assert is_valid("cs50p") == False

def test_cs5000():
    assert is_valid("cs5000") == True

def test_50cs():
    assert is_valid("50cs") == False

def test_c50():
    assert is_valid("c50") == False

def test_cs05():
    assert is_valid("cs05") == False

def test_cs50000():
    assert is_valid("cs50000") == False

def test_cs5_0():
    assert is_valid("cs5-0") == False
