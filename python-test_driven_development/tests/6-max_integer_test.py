#!/usr/bin/python3
"""
Unittest for max_integer(list=[])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing max_integer function"""

    def test_regular_list(self):
        """Test regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed_list(self):
        """Test list with both positive and negative integers"""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_repeated_elements(self):
        """Test a list with repeated elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_at_beginning(self):
        """Test a list with the maximum at the beginning"""
        self.assertEqual(max_integer([99, 1, 2, 3]), 99)

    def test_one_negative_number(self):
        """Test a list with one negative number"""
        self.assertEqual(max_integer([-8, 1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()
