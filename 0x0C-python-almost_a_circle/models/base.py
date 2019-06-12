#!/usr/bin/python3

"""A module for Base class"""

import json
from os import path


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        list_dict = []

        if list_objs  None:
            for i in list_objs:
                list_dict.append(i.to_dictionary())

        j_string = cls.to_json_string(list_dict)

        with open(filename, mode='w') as f:
            f.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        list_dict = json.loads(json_string)
        return list_dict

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls(8, 5, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        my_list = []

        filename = cls.__name__ + ".json"
        if path.isfile(filename) is not None:
            with open(filename, encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
            for dict in list_dict:
                my_list.append(cls.create(**dict))
        return my_list
