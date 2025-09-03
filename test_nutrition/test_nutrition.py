from nutrition import get_calories

def test_apple():
    assert get_calories("apple") == 130

def test_banana():
    assert get_calories("banana") == 110

def test_watermelon():
    assert get_calories("watermelon") == 80

def test_case_insensitivity():
    # test case insensitivity
    assert get_calories("APPLE") == 130
    assert get_calories("BaNaNa") == 110
    assert get_calories("WATERMELON") == 80

def test_unknown():
    # test unknown fruit
    assert get_calories("unknown") is None

def test_whitespace():
    # test input with leading/trailing whitespace
    assert get_calories("  apple") == 130
    assert get_calories("banana  ") == 110
    assert get_calories("  watermelon  ") == 80
