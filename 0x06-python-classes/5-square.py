#!/usr/bin/python3


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize class"""
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """To retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size != 0:
            for i in range(self.area()):
                print("#", end="\n" if (i+1) % self.__size == 0 else "")
        else:
            print("")
