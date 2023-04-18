#!/usr/bin/python3
"""base module"""
import json


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
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """json str to dict"""
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class initiated with attr alredy set
        Args:
           dictionary = key/value pair attribute to intialize
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instance"""
        filname = cls.__name__ + '.json'
        new = []

        try:
            with open(filname) as f:
                content = f.read()

        except:
            return new

        json_file = Base.from_json_string(content)
        for obj in json_file:
            new.append(cls.create(**obj))
        return new
