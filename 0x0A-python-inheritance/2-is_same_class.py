#!/usr/bin/python3

"""
A module for is_same_class.
"""


def is_same_class(obj, a_class):
    """A method that returns True if the object is exactly an instance of the
    specified class; otherwise False."""
    return type(obj) is a_class
