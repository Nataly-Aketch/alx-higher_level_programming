#!/usr/bin/python3
"""this module defines a class rectangle"""


class Rectangle:
    """this class defines a rectangle based on task 2"""
    def __init__(self, width=0, height=0):
        """Initializes a class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if 0 in (self.__width, self.__height):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return (self.__height - 1) * ("#" * self.__width + '\n') \
            + "#" * self.__width

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
