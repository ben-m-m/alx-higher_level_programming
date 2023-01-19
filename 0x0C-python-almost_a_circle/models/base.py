#!/usr/bin/python3
"""base module"""


class Base:
    """base for all other classes in this project
    attributes:
        __nb_objects (int): number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing a new base
        Args:
            id (int): The identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
