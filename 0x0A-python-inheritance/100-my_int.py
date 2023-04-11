#!/usr/bin/python3
"""defines a class MyInt"""


class MyInt(int):
    """class that inherits from int"""

    def __eq__(self, obj):
        """returns false if values are equal"""
        return False

    def __ne__(self, obj):
        """returns true if values are not equal"""
        return True
