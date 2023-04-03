#!/usr/bin/python3
"""This module contains definition of class rectangle"""


class Rectangle:
    """Defines a rectangle based on task 1"""
    def __init__(self, width, height):
        """Initializes a class rectangle"""
        self.width = width
        self.height = height

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

    def area(self):
        """computes area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """computes perimiter od a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
