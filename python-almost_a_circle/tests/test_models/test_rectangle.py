#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
import json
import sys
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch, MagicMock

class TestRectangle(unittest.TestCase):

    def test_valid_dimensions_two_values(self):
        """Test width and height"""
        rectangle = Rectangle(15, 77)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 77)

    def test_valid_dimensions_four_values(self):
        """Test width, height, x and y"""
        rectangle = Rectangle(15, 30, 7, 7)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 30)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 7)

    def test_valid_dimensions_five_values(self):
        """Test width, height, x, y, and id"""
        rectangle = Rectangle(15, 30, 7, 7, 123)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 30)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 7)
        self.assertEqual(rectangle.id, 123)



if __name__ == '__main__':
    unittest.main()
