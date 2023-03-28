#!/usr/bin/python3
"""Definining class square"""


class Square:
    """class with size as attribute"""
    def __init__(self, size=0):
        """Initialize the class"""
        self.__size = size

    @property
    def size(self):
        """this method accesses and returns the values of an attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """this method changes values of an attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates area of square"""
        return self.__size ** 2
