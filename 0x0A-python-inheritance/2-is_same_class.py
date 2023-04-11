#!/usr/bin/python3
"""contains a function that check if an object is
exactly an instance of a class"""


def is_same_class(obj, a_class):
    """return true is obj is an instance of the class
    a_class otherwise false"""
    if type(obj) == a_class:
        return True
    else:
        return False
