#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square with size validation and printing capability."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size  # passe par le setter

    @property
    def size(self):
        """Return the current size of the square."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Set the size of the square with checks."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = value

    def area(self):
        """Return the area of the square."""
        return pow(self._Square__size, 2)

    def my_print(self):
        """Print the square using # characters."""
        if self._Square__size == 0:
            print()
            return

        count = 0
        while count < self._Square__size:
            print("#" * self._Square__size)
            count += 1
