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
