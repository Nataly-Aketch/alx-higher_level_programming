#!/usr/bin/python3
"""this module contains a functions that reads a text file"""


def read_file(filename=""):
    """this functions opens and reads a file filename"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
