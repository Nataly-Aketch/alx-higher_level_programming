#!/usr/bin/python3
"""defines a function that returns a dictionary description
with simple data structures(list, string, bool"""


def class_to_json(obj):
    """obj - class instance to be converted"""
    return vars(obj)
