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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class."""

    def __init__(self, width, height):
        """Initialize the rectangle class."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A method that returns the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """A method that creates a string object from a given object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
