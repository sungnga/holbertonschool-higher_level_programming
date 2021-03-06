#!/usr/bin/python3
import math


class MagicClass:
    """MagicClass class"""
    def __init__(self, radius=0):
        """Initialize class"""
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Returns the area of a circle"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference of a circle"""
        return (2 * math.pi) * self._MagicClass__radius
