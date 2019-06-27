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

        if list_objs is not None:
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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 3)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        my_list = []

        filename = cls.__name__ + ".json"
        if path.exists(filename):
            with open(filename, encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
            for dict in list_dict:
                my_list.append(cls.create(**dict))
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        list_dict = []

        if list_objs is not None:
            for i in list_objs:
                list_dict.append(i.to_dictionary())

        j_string = cls.to_json_string(list_dict)

        with open(filename, mode='w') as f:
            f.write(j_string)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        my_list = []

        filename = cls.__name__ + ".csv"
        if path.exists(filename):
            with open(filename, encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
            for dict in list_dict:
                my_list.append(cls.create(**dict))
        return my_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Opens a window and draws all the Rectangles and Squares'''

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        position = t.position()
        t.color("orange")
        turtle.Screen().colormode(255)
        t.shape("turtle")
        t.pensize(2)
        t.fillcolor("purple")

        for o in (list_rectangles + list_squares):
            t.setposition(0, 0)
            t.color((randrange(255), randrange(255), randrange(255)))
            Base.drawRect(t, o)
            time.sleep(2)
        time.sleep(10)

    @staticmethod
    def drawRect(t, rect):
        t.setposition(rect.x, rect.y)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
