#!/usr/bin/python3

# Import the BaseGeometry class from the module 7-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Define the Rectangle class that inherits from BaseGeometry
class Rectangle(BaseGeometry):
    # Initialization method for Rectangle
    def __init__(self, width, height):
        # Use the inherited integer_validator method to ensure width is a positive integer
        self.integer_validator("width", width)
        # Use the inherited integer_validator method to ensure height is a positive integer
        self.integer_validator("height", height)
        # Define private attributes __width and __height
        self.__width = width
        self.__height = height
