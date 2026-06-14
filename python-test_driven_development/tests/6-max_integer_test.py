#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test mixed integers."""
        self.assertEqual(max_integer([-10, 5, 20, -3]), 20)

    def test_max_at_beginning(self):
        """Test max at beginning."""
        self.assertEqual(max_integer([10, 5, 3, 1]), 10)

    def test_max_at_middle(self):
        """Test max at middle."""
        self.assertEqual(max_integer([1, 10, 3, 2]), 10)

    def test_float_values(self):
        """Test float values."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_string(self):
        """Test string."""
        self.assertEqual(max_integer("Bash"), "s")


if __name__ == "__main__":
    unittest.main()
