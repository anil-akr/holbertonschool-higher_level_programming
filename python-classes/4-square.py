#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Initialize a square with validated size"""
        self._size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current square area"""
        return self.__size ** 2
