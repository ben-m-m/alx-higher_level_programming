#!/usr/bin/python3
"""defines a rectangle
area and perimeter"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """initialize a rectangle
        args:
        width(int): width of rectangle
        height(int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter: gets width value"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter: sets width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter: gets height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter: sets height value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
