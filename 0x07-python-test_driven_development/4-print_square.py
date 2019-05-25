#!/usr/bin/python3

"""
    This module prints a square with the character # with the
    following methods:
    print_square
"""


def print_square(size):
    """
    Prints a square with the character #.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            for col in range(size):
                print("#", end="")
            print()
