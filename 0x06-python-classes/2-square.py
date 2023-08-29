#!/usr/bin/python3
"""Class that defines a square by its size"""
class Square:
    def __init__(self, size=0):
        """
        Type and value validation in if else tree
        
        Args:
            size (int): square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
