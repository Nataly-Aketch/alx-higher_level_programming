#!/usr/bin/python3
"""Defining a class"""


class Square:
    """Defines a square based on task 0"""

    def __init__(self, size):
        """Initialized a private attribute size that is, it can only
        be used by the owner"""
        self.__size = size
