#!/usr/bin/python3
"""defines a function that returns object represented
string"""
import json


def from_json_string(my_str):
    """returns string rep of JSON string my_str"""
    return json.loads(my_str)
