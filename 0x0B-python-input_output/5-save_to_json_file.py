#!/usr/bin/python3
"""defines a function that writes an object to a text file
using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes my_obj to filename"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
