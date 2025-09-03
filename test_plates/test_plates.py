from plates import is_valid

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
def test_invalid_characters():
    assert is_valid("AB!23") == False  # contains special character
    assert is_valid("AB 123") == False  # contains space

def test_first_number_zero():
    assert is_valid("AB0123") == False

def test_all_numbers():
    assert is_valid("123456") == False

def test_mixed_valid():
    assert is_valid("AB123C") == False

