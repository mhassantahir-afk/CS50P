from bank import value

def test_hello():
    assert value("hello") == 0

def test_Hello():
    assert value("Hello!") == 0

def test_w():
    assert value("whatsup!") == 100

def test_hi():
    assert value("hi") == 20
