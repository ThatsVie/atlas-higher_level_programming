#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        obj = Base(id=1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty(self):
        result = Base.to_json_string([{'id': 1, 'name': 'test'}])
        self.assertEqual(result, '[{"id": 1, "name": "test"}]')

    def test_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{'id': 89}])

    def test_from_json_string_valid_list(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['id'], 89)

if __name__ == '__main__':
    unittest.main()
