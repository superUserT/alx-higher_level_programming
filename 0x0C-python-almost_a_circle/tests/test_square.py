#!/usr/bin/python3
"""Tests for the Square class with unittest"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_str(self):
        square = Square(4, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 4")

    def test_size_property(self):
        square = Square(3)
        square.size = 6
        self.assertEqual(square.size, 6)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_size_property_validation(self):
        square = Square(3)
        with self.assertRaises(ValueError):
            square.size = -1
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()