#!/usr/bin/python3
"""defines a class student"""


class Student():
    """class containing public instance attributes and method"""
    def __init__(self, first_name, last_name, age):
        """initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict representation of class student"""
        return self.__dict__
