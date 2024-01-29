#!/usr/bin/python3
"""Unittest for square.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init_with_valid_arguments(self):
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)
        self.assertEqual(obj.id, 4)

    def test_init_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)

if __name__ == '__main__':
    unittest.main()
