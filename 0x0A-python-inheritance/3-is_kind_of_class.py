#!/usr/bin/python3
"""my module"""


def is_kind_of_class(obj, a_class):
    """checks if its exact the same or inherited
    args:
        obj: object to check
        a_class: the class to verify instance of
    return:
        True if obj is an instance of class or
        inherited class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
