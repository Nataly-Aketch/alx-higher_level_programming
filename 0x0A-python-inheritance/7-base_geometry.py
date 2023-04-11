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
