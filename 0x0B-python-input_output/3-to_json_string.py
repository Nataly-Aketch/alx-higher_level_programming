#!/usr/bin/python3
"""contains a function that returns JSON representation
of a string"""
import json


def to_json_string(my_obj):
    """returns JSON representation of my_obj"""
    return json.dumps(my_obj)
