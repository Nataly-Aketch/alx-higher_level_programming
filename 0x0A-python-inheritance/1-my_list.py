#!/usr/bin/python3
"""This module contains a class that employs inheritance"""


class MyList(list):
    """This is a subclass of list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
