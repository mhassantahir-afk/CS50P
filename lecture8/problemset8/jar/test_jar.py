from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.cookies == 0
    jar.deposit(10)
    assert jar.cookies == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.withdraw(5) == 5
    with pytest.raises(ValueError):
        jar.withdraw(10)
