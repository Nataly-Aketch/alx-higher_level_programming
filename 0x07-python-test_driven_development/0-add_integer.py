#!/usr/bin/python3
"""This module contains a function that adds integers while
also perfoming a series of edge cases for TDD"""


def isnan(num):
    """checks for NaN"""
    return num != num


def add_integer(a, b=98):
    """this functions adds two integers or floats, casts floats to
    ints before adding and raises errors if a or b aren't ints or floats
    """
    list1 = [a, b]
    for i in range(len(list1)):
        if not isinstance(list1[i], (int, float)) or \
                isinstance(list1[i], bool) or isnan(list1[i]):
            raise TypeError("{} must be an integer"
                            .format("a" if i == 0 else "b"))
        if list1[i] + 1 == list1[i]:
            raise OverflowError("{} is too large"
                                .format("a" if i == 0 else "b"))
    return int(a) + int(b)
