#!/usr/bin/python3
"""This module contains a function that prints a sentence"""


def say_my_name(first_name, last_name=""):
    """Prints my name is first_name last_name"""
    list1 = [first_name, last_name]
    for w in range(len(list1)):
        if not isinstance(list1[w], str):
            raise TypeError("{} must be a string"
                            .format("first_name" if w == 0 else "last_name"))
    print("My name is {} {}".format(first_name, last_name))
