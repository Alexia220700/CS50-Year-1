from twttr import shorten

def test_shorten_mixed_case():
    # test a string with mixed case vowels
    assert shorten("Hello World") == "Hll Wrld"

def test_shorten_numbers_and_symbols():
    # Test a string with numbers and symbols (no vowels)
    assert shorten("123!@#") == "123!@#"

def test_shorten_all_vowels():
    # Test a string with only vowels
    assert shorten("AEIOUaeiou") == ""

def test_shorten_lowercase_vowels():
    # Test a string with lowercase vowels
    assert shorten("banana") == "bnn"
