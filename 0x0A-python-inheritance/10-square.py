#!/usr/bin/python3
"""class square that inherits from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square
    inherits from Rectangle
    """

    def __init__(self, size):
        """initialize a square
        args:
            size(int): square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """computes area of square"""
        return self.__size ** 2
