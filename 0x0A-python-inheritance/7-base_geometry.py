#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """instance that raises an exception"""
    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        args:
            name(str): name of parameter
            value(int): parameter to validate
        return:
            TypeError: if value not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
