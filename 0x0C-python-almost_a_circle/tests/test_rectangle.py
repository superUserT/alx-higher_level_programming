#!/usr/bin/python3
"""Tests for Rectangle class with unittest"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(4, 5, 1, 2, 3)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 3)

    def test_str(self):
        rectangle = Rectangle(3, 7, 2, 1, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (4) 2/1 - 3/7")

    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)


    def test_size_property(self):
        rectangle = Rectangle(3, 4)
        rectangle.width = 5
        rectangle.height = 6
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)

    def test_size_property_validation(self):
        rectangle = Rectangle(3, 4)
        with self.assertRaises(ValueError):
            rectangle.width = -1
        with self.assertRaises(TypeError):
            rectangle.width = "invalid"

    def test_to_dictionary(self):
        rectangle = Rectangle(3, 4, 1, 2, 5)
        rect_dict = rectangle.to_dictionary()
        expected_dict = {
            "id": 5,
            "width": 3,
            "height": 4,
            "x": 1,
            "y": 2
        }
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
