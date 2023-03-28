#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Contains private instance attribute and methods"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes class square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif tuple[0] < 0 and tuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        for row in range(self.__size):
            if row < self.__size:
                print((" ") * self.__position[0], end="")
            else:
                print((" ") * self.__position[0], end="\n")
            for col in range(self.__size):
                if col < self.__size:
                    print("#", end="")
                else:
                    print("#", end="\n")
            print()
