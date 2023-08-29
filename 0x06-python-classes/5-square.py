#!/usr/bin/python3
"""Class that defines a square by its size"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Validation"""
        self.__size = size

    @property
    def size(self):
        """Get the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Represents the area of a square"""
    def area(self):
        """Returns the square of a square"""
        return self.__size ** 2
    """Prints the area of a square """
    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)
