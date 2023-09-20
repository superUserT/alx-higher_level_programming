#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project."""
import json
from os import path


class Base:
    ''' private class attribute '''
    __nb_objects = 0
    ''' class constructor '''
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of a JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary"""
        if cls.__name__ == "Rectangle":
            objct = cls(1, 1)
        elif cls.__name__ == "Square":
            objct = cls(1)

        objct.update(**dictionary)
        return objct

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename, "r") as file:
            obj = Base.from_json_string(file.read())
        list = [cls.create(**dict) for dict in obj]
        return list
