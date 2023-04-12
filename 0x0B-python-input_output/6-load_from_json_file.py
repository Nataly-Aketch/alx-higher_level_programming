#!/usr/bin/python3
"""define a function that creates an object from
a JSON file"""
import json


def load_from_json_file(filename):
    """creates object from filename"""
    with open(filename) as f:
        return json.load(f)
