#!/usr/bin/python3

"""A module for Base class"""


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
