#!/usr/bin/python3
"""contains a function that opens a file in append mode"""


def append_write(filename="", text=""):
    """opens filename and appends text to it"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
