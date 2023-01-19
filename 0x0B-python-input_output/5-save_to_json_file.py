#!/usr/bin/python3
"""write object to txt file
in json representation"""
import json


def save_to_json_file(my_obj, filename):
    """write obj to txt using json rep
    args:
        my_obj: object to be written
        filename: txt file written into
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
