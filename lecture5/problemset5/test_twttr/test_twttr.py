from twttr import shorten

def test_something():
    assert shorten("something") == "smthng"

def test_twitter():
    assert shorten("Twitter") == "Twttr"

def test_hello():
    assert shorten("hello") == "hll"

def test_caputalvowel():
    assert shorten("TwIttEr") == "Twttr"

def test_numbers():
    assert shorten("something123") == "smthng123"

def test_punc():
    assert shorten("hello, world!") == "hll, wrld!"
