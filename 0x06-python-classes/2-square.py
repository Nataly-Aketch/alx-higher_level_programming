#!/usr/bin/python3
"""Definining class square"""


class Square:
    """class with size as attribute"""
    def __init__(self, size=0):
        """Initialize the class"""
        self.setter(size)

    def getter(self, size):
        """this method accesses and returns the values of an attribute"""
        return self.__size

    def setter(self, size):
        """this method changes values of an attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
