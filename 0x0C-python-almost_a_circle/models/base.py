#!/usr/bin/python3
"""defines a class base"""
import json


class Base():
    """this class contains nb_objects as a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serializer - returns json representations of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation of list_objs to file
        with name <class-name>.json"""
        if list_objs is None:
            objs = cls.to_json_string(None)
        else:
            objs = cls.to_json_string([i.to_dictionary() for i in list_objs])

        new_file = '{}.{}'.format(cls.__name__, 'json')
        with open(new_file, 'w') as f:
            f.write(objs)
        return new_file

    @staticmethod
    def from_json_string(json_string):
        """deserializer - converts json representation to python object"""
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        employs update method to assign attributes by creating a
        dummy instance"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        new_file = cls.__name__ + ".json"
        try:
            with open(new_file, "r") as f:
                lst = cls.from_json_string(f.read())
                return [cls.create(**d) for d in lst]
        except Exception:
            return []
