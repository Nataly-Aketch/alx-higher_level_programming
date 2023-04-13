#!/usr/bin/python3
"""defines a function that inserts a line to a file
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts new_string into filename after search_string"""
    with open(filename, "r+") as f:
        f.seek(0)
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] += new_string
        f.seek(0)
        for w in lines:
            f.write(w)
