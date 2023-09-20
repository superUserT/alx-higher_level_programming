#!/usr/bin/python3
"""Tests for the Base class with unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_init(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

        obj3 = Base(10)
        self.assertEqual(obj3.id, 10)

    def test_to_json_string(self):
        obj1 = Rectangle(4, 5)
        obj2 = Rectangle(1, 2)
        obj3 = Square(3)
        obj_list = [obj1, obj2, obj3]
        
        json_string = Base.to_json_string([obj.to_dictionary() for obj in obj_list])
        self.assertEqual(json_string, '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 3, "size": 3, "x": 0, "y": 0}]')

    def test_save_to_file(self):
        obj1 = Rectangle(4, 5)
        obj2 = Rectangle(1, 2)
        obj_list = [obj1, obj2]

        Rectangle.save_to_file(obj_list)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}]'
        obj_list = Base.from_json_string(json_string)
        
        self.assertEqual(len(obj_list), 2)
        self.assertIsInstance(obj_list[0], Rectangle)
        self.assertIsInstance(obj_list[1], Rectangle)

    def test_create(self):
        dictionary = {"id": 3, "width": 4, "height": 5, "x": 1, "y": 2}
        obj = Base.create(**dictionary)

        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 2)

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
