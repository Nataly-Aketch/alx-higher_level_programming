#!/usr/bin/python3
"""this module contains a function that creates and writes
to a file"""


def write_file(filename="", text=""):
    """filename is the file to be created and written to
    text is contents to be written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
