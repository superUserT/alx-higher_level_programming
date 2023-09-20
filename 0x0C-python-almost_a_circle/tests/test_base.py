#!/usr/bin/python3
"""Tests for the Base class with unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Class tests"""

    def test_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(125)
        self.assertEqual(base3.id, 125)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_exists(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])



    def test_load_from_file(self):
        obj1 = Rectangle(4, 5)
        obj2 = Rectangle(1, 2)
        obj_list = [obj1, obj2]

        Rectangle.save_to_file(obj_list)

        loaded_list = Rectangle.load_from_file()
        self.assertEqual(len(loaded_list), 2)
        self.assertIsInstance(loaded_list[0], Rectangle)
        self.assertIsInstance(loaded_list[1], Rectangle)


if __name__ == "__main__":
    unittest.main()
