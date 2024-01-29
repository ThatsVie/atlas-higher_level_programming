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

    def test_string_representation(self):
        square = Square(9, 2, 3, 88)
        self.assertEqual(str(square), "[Square] (88) 2/3 - 9")

    def test_to_dict_representation(self):
        square = Square(20, 10, 10, 99)
        self.assertEqual(square.to_dictionary(), {'id': 99, 'size': 20, 'x': 10, 'y': 10})

    def test_update_attributes(self):
        square = Square(45, 18, 18, 9)
        square.update(111, 42, 42, 33)

        self.assertEqual(square.id, 111)
        self.assertEqual(square.size, 42)
        self.assertEqual(square.x, 42)
        self.assertEqual(square.y, 33)

    def test_create_instance_from_dictionary(self):
        square = Square.create(**{'id': 33})
        self.assertEqual(square.id, 33)

    def test_save_to_file_with_none(self):
        with patch('builtins.open', create=True) as mock_open:
            Square.save_to_file(None)

            mock_open.assert_called_once_with('Square.json', mode='w', encoding='utf-8')

            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            loaded_data = json.loads(write_args[0])

            self.assertEqual(loaded_data, [])


if __name__ == '__main__':
    unittest.main()
