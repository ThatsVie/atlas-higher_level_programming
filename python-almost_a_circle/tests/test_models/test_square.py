#!/usr/bin/python3
"""Unittest for square.py"""
import unittest
import json
import sys
from models.square import Square
from io import StringIO
from unittest.mock import patch, MagicMock

class TestSquare(unittest.TestCase):

    def test_size_1(self):
        square = Square(10)
        self.assertEqual(square.size, 10)

    def test_size_2(self):
        square = Square(75, 1)
        self.assertEqual(square.size, 75)
        self.assertEqual(square.x, 1)

    def test_size_3(self):
        square = Square(30, 2, 3)
        self.assertEqual(square.size, 30)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_size_4(self):
        square = Square(40, 2, 3, 55)
        self.assertEqual(square.size, 40)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 55)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("string")

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Square(5, "string")

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Square(2, 3, "string")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-8)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -7)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 5, -8)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)


if __name__ == '__main__':
    unittest.main()
