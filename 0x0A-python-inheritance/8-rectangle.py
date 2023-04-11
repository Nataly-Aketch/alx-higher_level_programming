#!/usr/bin/python3
""" This module contains an empty class"""


class BaseGeometry():
    """this class contains a function area and int validator"""
    def area(self):
        """raise implementation error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if a value is an int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes rectangle class"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
