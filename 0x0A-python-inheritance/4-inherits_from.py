#!/usr/bin/python3
"""My module"""


def inherits_from(obj, a_class):
    """checks if object is from inherited class
    direct/indirect
    args:
        obj: object to check
        a_class: class to match with
    returns:
        True if object is instance of class
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
