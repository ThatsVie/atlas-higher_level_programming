#!/usr/bin/python3
"""Unittest for square.py"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_init(self):
        obj = Square(1)
        self.assertIsInstance(obj, Square)

    def test_square_init_with_args(self):
        obj = Square(1, 2, 3, 4)
        self.assertIsInstance(obj, Square)

    def test_square_init_with_invalid_args(self):
        with self.assertRaises(ValueError):
            Square("1")
        with self.assertRaises(ValueError):
            Square(1, "2")
        with self.assertRaises(ValueError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(1, 2, 3, "4")

    def test_square_init_with_negative_values(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_str(self):
        obj = Square(1, 2, 3, 4)
        self.assertEqual(str(obj), "[Square] (4) 2/3 - 1")

    def test_square_display(self):
        obj = Square(2)
        self.assertEqual(obj.display(), None)  # Check if runs without errors

    def test_square_display_without_xy(self):
        obj = Square(2)
        self.assertEqual(obj.display(), None)

    def test_square_display_without_y(self):
        obj = Square(2)
        self.assertEqual(obj.display(), None)

    def test_square_to_dictionary(self):
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_square_update(self):
        obj = Square(1, 2, 3, 4)
        obj.update(89)
        self.assertEqual(obj.id, 89)

    def test_square_update_multiple_args(self):
        obj = Square(1, 2, 3, 4)
        obj.update(89, 1, 2, 3)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_square_update_kwargs(self):
        obj = Square(1, 2, 3, 4)
        obj.update(**{'id': 89})
        self.assertEqual(obj.id, 89)

    def test_square_create(self):
        obj = Square.create(id=89, size=1, x=2, y=3)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_square_save_to_file(self):
        Square.save_to_file([Square(1)])

    def test_square_load_from_file_not_exist(self):
        obj_list = Square.load_from_file()
        self.assertEqual(obj_list, [])

    def test_square_load_from_file_exist(self):
        Square.save_to_file([Square(1)])
        obj_list = Square.load_from_file()
        self.assertIsInstance(obj_list, list)
        self.assertIsInstance(obj_list[0], Square)

if __name__ == '__main__':
    unittest.main()
