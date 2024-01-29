#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
import json
import sys
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch, MagicMock

class TestRectangle(unittest.TestCase):

    def test_valid_dimensions_two_values(self):
        """Test width and height"""
        rectangle = Rectangle(15, 77)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 77)

    def test_valid_dimensions_four_values(self):
        """Test width, height, x and y"""
        rectangle = Rectangle(15, 30, 7, 7)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 30)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 7)

    def test_valid_dimensions_five_values(self):
        """Test width, height, x, y, and id"""
        rectangle = Rectangle(15, 30, 7, 7, 123)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 30)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 7)
        self.assertEqual(rectangle.id, 123)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 30, 7, 7)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(30, "invalid", 7, 7)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 30, "invalid", 7)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 30, 123, "invalid")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -5)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -3, 4)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 3, -6)

    def test_calculate_area(self):
        rec = Rectangle(8, 15)
        result = rec.area()
        self.assertEqual(result, 120)

    def test_string_representation(self):
        rec = Rectangle(8, 15, 4, 6, 987)
        self.assertEqual(str(rec), "[Rectangle] (987) 4/6 - 8/15")

    def test_display_without_position(self):
        rec = Rectangle(5, 3)

        output_buffer = StringIO()
        sys.stdout = output_buffer

        rec.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_buffer.getvalue(), "#####\n#####\n#####\n")

    def test_display_with_position(self):
        rec = Rectangle(6, 4, 3, 1, 2)

        output_buffer = StringIO()
        sys.stdout = output_buffer

        rec.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(output_buffer.getvalue(), "\n   ######\n   ######\n   ######\n   ######\n")

    def test_to_dictionary_representation(self):
        rec = Rectangle(5, 8, 3, 3, 456)

        self.assertEqual(rec.to_dictionary(), {'id': 456, 'width': 5, 'height': 8, 'x': 3, 'y': 3})

    def test_update_attributes(self):
        rec = Rectangle(8, 5, 4, 2, 123)
        rec.update(987, 7, 3, 4, 5)

        self.assertEqual(rec.id, 987)
        self.assertEqual(rec.width, 7)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)

    def test_create_instance_from_dictionary(self):
        rec = Rectangle.create(**{'id': 654})

        self.assertEqual(rec.id, 654)

    def test_save_to_file_with_none(self):
        with patch('builtins.open', create=True) as mock_open:
            Rectangle.save_to_file(None)

            mock_open.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')

            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            written_json = json.loads(write_args[0])

            self.assertEqual(written_json, [])

    def test_save_to_file_with_empty_list(self):
        with patch('builtins.open', create=True) as mock_open:
            Rectangle.save_to_file([])

            mock_open.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')

            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            loaded_data = json.loads(write_args[0])

            self.assertEqual(loaded_data, [])

    def test_save_to_file_with_single_rectangle_instance(self):
        rec = Rectangle(2, 3)

        with patch('builtins.open', create=True) as mock_open:
            Rectangle.save_to_file([rec])

            mock_open.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')

            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            loaded_data = json.loads(write_args[0])

            self.assertEqual(len(loaded_data), 1)
            self.assertEqual(loaded_data[0]['id'], rec.id)
            self.assertEqual(loaded_data[0]['width'], rec.width)
            self.assertEqual(loaded_data[0]['height'], rec.height)
            self.assertEqual(loaded_data[0]['x'], rec.x)
            self.assertEqual(loaded_data[0]['y'], rec.y)

    @patch('builtins.open', new_callable=MagicMock)
    def test_load_from_file_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        mock_open.return_value.__enter__.return_value.read.return_value = ""

        file_contents = Rectangle.load_from_file()

        mock_open.assert_called_once_with('Rectangle.json', 'r')

        self.assertEqual(file_contents, [])


if __name__ == '__main__':
    unittest.main()
