#!/usr/bin/python3

"""
A module for BaseGeometry class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class."""

    def __init__(self, size):
        """Initialize the square class."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a rectangle."""
        return (self.__size ** 2)
