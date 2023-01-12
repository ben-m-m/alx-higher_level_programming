#!/usr/bin/python3
"""Module of function that adds 2 integers"""


def add_integer(a, b=98):
    """Function that adds two integers or floats
    Returns sum of numbers
    raises:
         TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be a float")

    return (int(a) + int(b))
