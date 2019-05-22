#!/usr/bin/python3


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """To retrieve position"""
        return self.__size

    @position.setter
    def position(self, value):
        """To set position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
        else:
            print("")
