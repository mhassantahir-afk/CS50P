from numb3rs import validate

def test_1():
    assert validate("1.1.1.1") == True

def test_2():
    assert validate("q.123.123.123") == False

def test_3():
    assert validate("256.255.155.155") == False

def test_4():
    assert validate("25.255.255.256") == False
