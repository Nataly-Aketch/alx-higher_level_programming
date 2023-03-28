#!/usr/bin/python3
"""defining class square"""


class Square:
    """Contains size as a private attribute and a public instance
    method to calculate area"""
    def __init__(self, size=0):
        """Initilializes size"""
        self.__size = size

    def area(self):
        """Calculates area of a square"""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size ** 2
