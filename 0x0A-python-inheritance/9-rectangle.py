#!/usr/bin/python3

"""
A module for BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class."""

    def __init__(self, width, height):
        """Initialize the rectangle class."""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """A method that returns the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """A method that creates a string object from a given object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
