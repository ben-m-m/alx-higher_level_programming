#!/usr/bin/python3
"""base module"""
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        list_dictionaries - is a list of dictionaries
        Returns: JSON string representation of list_dictionaries
                otherwise returns "[]" if None or empty
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        list_objs - list of instances inherited from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(lst_dicts))
