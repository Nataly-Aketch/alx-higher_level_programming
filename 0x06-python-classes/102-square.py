#!/usr/bin/python3
"""Definining a class square"""


class Square:
    """square class with private instance attribute size"""
    def __init__(self, size=0):
        """Initializes a class square"""
        self.__size = size

    def area(self):
        """calculates area of a square"""
        return self.__size ** 2

    def __lt__(self, other):
        """less than or greater than comparators"""
        return self.area() < other.area()

    def __eq__(self, other):
        """equality to comparator"""
        return self.area() == other.area()

    def __le__(self, other):
        """less than or equal to comparators"""
        return self.area() <= other.area()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
