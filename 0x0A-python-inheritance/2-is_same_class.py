#!/usr/bin/python3
"""module that finds
if the object is exactly an
instance of the specified class
"""


def is_same_class(obj, a_class):
    """checks if its exact
    args:
        obj: object to look at
        a_class: class to verify the instance of
    return:
        True if object is exact
        False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
