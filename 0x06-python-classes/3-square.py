#!/usr/bin/python3


class Square:
    """A square class"""
    __size = None

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
