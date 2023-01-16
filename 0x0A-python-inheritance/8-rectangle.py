#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """initialize new rectangle
        args:
            width(int): rectangle width
            height(int): rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
