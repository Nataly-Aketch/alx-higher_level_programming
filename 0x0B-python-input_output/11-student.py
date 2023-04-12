#!/usr/bin/python3
"""defines a class student"""


class Student():
    """class containing public instance attributes and method"""
    def __init__(self, first_name, last_name, age):
        """initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieves dict representation of class student"""
        if attr is not None and type(attr) == list and \
                all(isinstance(i, str) for i in attr):
            return dict((k, getattr(self, k)) for k in attr if
                        hasattr(self, k))
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of of Student instance"""
        self.__dict__ = json
