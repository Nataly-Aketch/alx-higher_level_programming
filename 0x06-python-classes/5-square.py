#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Contains private instance attribute and methods"""
    def __init__(self, size=0):
        """Initializes class square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                if col < self.__size:
                    print("#", end="")
                else:
                    print("#", end="\n")
            print()
