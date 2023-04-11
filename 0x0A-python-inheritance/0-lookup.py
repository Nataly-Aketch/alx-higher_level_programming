#!/usr/bin/python3
"""This module contains a function that returns a list of
available modules and attributes of an object"""


def lookup(obj):
    """obj is the object to be checked. Returns a list object"""
    return dir(obj)
