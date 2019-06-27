#!/usr/bin/python3

"""A module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """To retrieve size"""
        return self.__width

    @size.setter
    def size(self, size):
        """To set size"""
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    def __str__(self):
        """Creates a string object from a given object"""
        end_string = "[Square] "
        end_string += "({}) ".format(self.id)
        end_string += "{:d}/{:d} - ".format(self.x, self.y)
        end_string += "{:d}".format(self.size)
        return end_string

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to each attribute"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]

        if "size" in kwargs:
            self.size = kwargs["size"]

        if "x" in kwargs:
            self.x = kwargs["x"]

        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """Creates string object from a given object"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
