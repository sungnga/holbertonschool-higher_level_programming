#!/usr/bin/python3

"""A module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """To retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """To retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """To set width"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """To retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """To set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for n in range(self.y):
            print()
        for i in range(self.height):
            for m in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Creates a string object from a given object"""
        end_string = "[Rectangle] "
        end_string += "({}) ".format(self.id)
        end_string += "{:d}/{:d} - ".format(self.x, self.y)
        end_string += "{:d}/{:d}".format(self.width, self.height)
        return end_string

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to each attribute"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]

        if "width" in kwargs:
            self.width = kwargs["width"]

        if "height" in kwargs:
            self.height = kwargs["height"]

        if "x" in kwargs:
            self.x = kwargs["x"]

        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary represenation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
