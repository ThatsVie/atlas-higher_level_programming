#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_with_valid_arguments(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)
        self.assertEqual(obj.id, 5)

    def test_init_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_init_with_missing_arguments_1(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2)

    def test_init_with_missing_arguments_2(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3)

    def test_init_with_missing_arguments_3(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4)

    def test_init_with_invalid_type_1(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_init_with_invalid_type_2(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_init_with_invalid_type_3(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_init_with_invalid_type_4(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

if __name__ == '__main__':
    unittest.main()
