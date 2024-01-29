#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        obj = Rectangle(1, 2)
        self.assertIsInstance(obj, Rectangle)

    def test_rectangle_init_with_args(self):
        obj = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(obj, Rectangle)

    def test_rectangle_init_with_invalid_args(self):
        with self.assertRaises(ValueError):
            Rectangle("1", 2)
        with self.assertRaises(ValueError):
            Rectangle(1, "2")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, "3")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_init_with_negative_values(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        obj = Rectangle(5, 10)
        self.assertEqual(obj.area(), 50)

    def test_rectangle_str(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(obj), "[Rectangle] (5) 3/4 - 1/2")

    def test_rectangle_display(self):
        obj = Rectangle(2, 2)
        self.assertEqual(obj.display(), None)  # checking runs without errors

    def test_rectangle_display_without_xy(self):
        obj = Rectangle(2, 2)
        self.assertEqual(obj.display(), None)

    def test_rectangle_display_without_y(self):
        obj = Rectangle(2, 2)
        self.assertEqual(obj.display(), None)

    def test_rectangle_to_dictionary(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_rectangle_update(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(89)
        self.assertEqual(obj.id, 89)

    def test_rectangle_update_multiple_args(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(89, 1, 2, 3, 4)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_rectangle_update_kwargs(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(**{'id': 89})
        self.assertEqual(obj.id, 89)

    def test_rectangle_create(self):
        obj = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_rectangle_save_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        # Checking file existence and content is skipped

    def test_rectangle_load_from_file_not_exist(self):
        obj_list = Rectangle.load_from_file()
        self.assertEqual(obj_list, [])

    def test_rectangle_load_from_file_exist(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        obj_list = Rectangle.load_from_file()
        self.assertIsInstance(obj_list, list)
        self.assertIsInstance(obj_list[0], Rectangle)

if __name__ == '__main__':
    unittest.main()
