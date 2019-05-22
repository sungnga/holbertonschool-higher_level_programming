#!/usr/bin/python3


class Node:
    """A node class"""

    def __init__(self, data, next_node=None):
        """Initialize class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """To retrieve data"""
        return self.__data

    @size.setter
    def data(self, value):
        """To set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """To retrieve data"""
        return self.__next_node

    @size.setter
    def next_node(self, value):
        """To set data"""
        if not isinstance(value, None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A SinglyLinkedList class"""

    def __init__(self):
        """Initialize class"""
        self.__head

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list
        (increasing order)"""
