#!/usr/bin/python3
"""student to json module
with attrs
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializes student class
        args:
            first_name: students first name
            last_name: students last name
            age(int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
