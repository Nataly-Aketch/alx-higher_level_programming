#!/usr/bin/python3
"""Module to find the max integer in a list
"""

def max_integer(list1=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None"""

    if list1 is None or not list1:
        raise TypeError("Args 1 can't be none")
    if len(list1) == 0:
        return None
    if not isinstance(list1, list):
        raise TypeError("Args 1 must be a list")
    for i in list1:
        if not isinstance(i, (int, float)) or isinstance(i, bool):
            raise TypeError("list should contain ints/floats")
    result = list1[0]
    i = 1
    while i < len(list1):
        if list1[i] > result:
            result = list1[i]
        i += 1
    return result
