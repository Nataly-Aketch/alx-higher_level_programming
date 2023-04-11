#!/usr/bin/python3
"""contains a function that check if an object is
an instance of a class"""


def is_kind_of_class(obj, a_class):
    """return true is obj is an instance of the class
    a_class otherwise false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
