import unittest
from scavengerhunt import simple_number_encrypt

class TestNumberEncryption(unittest.TestCase):

    # Tests for simple_number_encrypt
    def test_simple_encrypt_basic(self):
        self.assertEqual(simple_number_encrypt("123"), "ABC")
        self.assertEqual(simple_number_encrypt("85023"), "HE0BC")

    def test_simple_encrypt_with_non_digits(self):
        self.assertEqual(simple_number_encrypt("1a3b5"), "AaCbE")
        self.assertEqual(simple_number_encrypt("1-2-3"), "A-B-C")

    def test_simple_encrypt_edge_cases(self):
        self.assertEqual(simple_number_encrypt("0"), "0")
        self.assertEqual(simple_number_encrypt("9"), "I")
        self.assertEqual(simple_number_encrypt("10"), "A0")


if __name__ == '__main__':
    unittest.main()
