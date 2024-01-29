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

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 30, 7, 7)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(30, "invalid", 7, 7)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 30, "invalid", 7)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 30, 123, "invalid")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -5)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -3, 4)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 3, -6)

    def test_calculate_area(self):
        rec = Rectangle(8, 15)
        result = rec.area()
        self.assertEqual(result, 120)

    def test_string_representation(self):
        rec = Rectangle(8, 15, 4, 6, 987)
        self.assertEqual(str(rec), "[Rectangle] (987) 4/6 - 8/15")

    def test_display_without_position(self):
        rec = Rectangle(5, 3)

        output_buffer = StringIO()
        sys.stdout = output_buffer

        rec.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_buffer.getvalue(), "#####\n#####\n#####\n")


if __name__ == '__main__':
    unittest.main()
