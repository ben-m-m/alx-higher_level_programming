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

    def area(self):
        """computes the area of the rectangle instance"""
        return self.__width * self.__height

    def __str__(self):
        """returns a formatted string"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
