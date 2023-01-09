#!/usr/bin/python3
"""defines a square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initialize a new square
        args:
        size (int): Size of the new square."""
        self.size = size

    @property
    def size(self):
        """set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set property of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns current square area"""
        return (self.__size * self.__size)
