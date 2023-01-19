#!/usr/bin/python3
"""write module"""


def write_file(filename="", text=""):
    """write a string and return no
    of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
