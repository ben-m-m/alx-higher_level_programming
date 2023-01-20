#!/usr/bin/python3
"""Defines a rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs a rectangle class"""
        """
        Raises:
            TypeError: If either of width, height, x or y is not an int.
            ValueError: If either of width or height is <= 0
                and If x or y is < 0
        """

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

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """gets the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """returns the area value of Rectangle instance"""

        return self.width * self.height

    def display(self):
        """display # in rectangle form"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print('#', end="")for j in range(self.width)]
            print()

    def __str__(self):
        """Overriding str method from Base"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .formart(self.id, self.x, self.y, self.width, self.height)
