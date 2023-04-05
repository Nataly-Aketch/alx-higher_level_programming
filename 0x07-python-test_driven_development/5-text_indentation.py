#!/usr/bin/python3
"""This module contains a function that prints a text
with two new lines after given delimiters"""


def text_indentation(text):
    """splits text into two new lines if ?, : and . are found"""

    if text is None:
        raise TypeError("'Nonetype' object is not iterable")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delim = '?.:'
    buff = ""
    for c in text:
        if c in delim:
            buff += c + "\n\n"
        else:
            buff += c

    new_str = buff.split('\n')
    for w in new_str:
        print(w.strip())
