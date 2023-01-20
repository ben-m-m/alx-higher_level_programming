#!/usr/bin/python3
"""Defines a rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs a rectangle class"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        self.__width = value

    @property
    def height(self):
        """gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        self.__height = value

    @property
    def y(self):
        """gets the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        self.__y = value

    @property
    def x(self):
        """gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        self.__x = value
