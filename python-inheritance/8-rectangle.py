#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        # Validate width using BaseGeometry method
        self.integer_validator("width", width)

        # Validate height using BaseGeometry method
        self.integer_validator("height", height)

        # Private instance attributes
        self.__width = width
        self.__height = height
