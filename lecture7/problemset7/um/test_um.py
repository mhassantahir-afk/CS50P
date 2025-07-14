from um import count

def test_1():
    assert count("erm actually um um.") == 2

def test_2():
    assert count("erm actually umun") == 0

def test_3():
    assert count("um, um um.") == 3

def test_4():
    assert count("Um, Um.") == 2
