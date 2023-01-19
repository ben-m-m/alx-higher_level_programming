#!/usr/bin/python3
"""creates object from a json file"""
import json


def load_from_json_file(filename):
    """
    creates a python object fron
    json file
    args:
        filename: json file to load from
    """
    with open(filename, encoding="utf-8") as f:
        json.load(f)
