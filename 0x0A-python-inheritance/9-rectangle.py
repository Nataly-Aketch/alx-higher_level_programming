#!/usr/bin/python3
""" This module contains an empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes rectangle class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """prints string representation of the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """calculates area of a rectangle"""
        return self.__width * self.__height
