#!/usr/bin/python3
"""defines a square"""


class Square:
    """initialize a new square"""
    def __init__(self, size=0):
        """Initialize a new square.
        args:
        size (int): Size of the new square."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
