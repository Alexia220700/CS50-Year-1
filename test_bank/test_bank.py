from bank import value

def test_hello():
    assert value("hello") == 0

def test_h_but_not_hello():
    assert value("hi") == 20

def test_case_insensitivity():
    # Test case insensitivity
    assert value("HELLO") == 0
    assert value("hELLo") == 0
    assert value("HI") == 20
    assert value("hOw are you") == 20
    assert value("WHATS UP") == 100

def test_whitespace():
    # Test greeting with leading/trailing whitespace
    assert value("  hello") == 0
    assert value("hello  ") == 0
