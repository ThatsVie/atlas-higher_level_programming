#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):

    def test_auto_assign_id(self):
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(55)
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 55)

    def test_id_is_int(self):
        base_instance = Base(55)
        self.assertIsInstance(base_instance.id, int)

    def test_to_json_empty(self):
        with self.assertRaises(TypeError):
            instance = Base()
            json_dictionary = Base.to_json_string()

    @patch('sys.stdout', new_callable=StringIO)
    def test_to_json_string_with_none(self, mock_stdout):
        expected_output = "[]"
        result = Base.to_json_string(None)
        self.assertEqual(result, expected_output)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_from_json_string_with_none(self, mock_stdout):
        expected_output = []
        result = Base.from_json_string(None)
        self.assertEqual(result, expected_output)
        self.assertEqual(mock_stdout.getvalue(), "")

if __name__ == '__main__':
    unittest.main()
