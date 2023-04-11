#!/usr/bin/python3
"""Defines a class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size):
        """Initializes a class with ptivate attribute size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area of a square"""
        return self.__size ** 2
