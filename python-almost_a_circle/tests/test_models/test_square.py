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


if __name__ == '__main__':
    unittest.main()
