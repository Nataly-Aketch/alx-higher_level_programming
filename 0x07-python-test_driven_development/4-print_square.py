#!/usr/bin/python3
"""This module contains a function that prints a square using #"""


def print_square(size):
    """prints a square of size 'size' with '#'s"""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for i in range(size):
            print("#", end="")
        print()
