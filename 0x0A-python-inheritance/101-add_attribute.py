#!/usr/bin/python3
"""this module contains a functions that adds nw attribute"""


def add_attribute(obj, name, value):
    """sets name as value if obj has the __dict__ attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
