#!/usr/bin/python3

"""
A module for BaseGeometry class.
"""


class BaseGeometry():
    """A BaseGeometry class."""

    def area(self):
        """A method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates value."""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(value))


class Rectangle(BaseGeometry):
    """A rectangle class."""

    def __init__(self, width, height):
        """Initialize the rectangle class."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
