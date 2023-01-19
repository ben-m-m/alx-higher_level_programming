#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """appends a string and returns
    the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
