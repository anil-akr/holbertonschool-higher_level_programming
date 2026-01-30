#!/usr/bin/python3
"""Defines a Rectangle class with instance counting, customizable print
symbol, static method bigger_or_equal, and class method square."""


class Rectangle:
    """Represents a rectangle with width, height, and customizable print
    symbol."""

    number_of_instances = 0  # Compte le nombre d'instances vivantes
    print_symbol = "#"       # Symbole par défaut pour afficher le rectangle

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # ----- WIDTH -----
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # ----- HEIGHT -----
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # ----- METHODS -----
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with the symbol print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string representation to recreate the object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted and
        decrement the instance counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # ----- STATIC METHOD -----
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area.

        If both have the same area, return rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    # ----- CLASS METHOD -----
    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
