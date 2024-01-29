#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        # Remove any existing JSON files before each test
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass


    def test_auto_assign_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_auto_assign_id_multiple_instances(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_save_id_passed(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_empty(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_id(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_with_id(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{'id': 89}])

    def test_from_json_string_valid_list(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['id'], 89)

if __name__ == '__main__':
    unittest.main()
