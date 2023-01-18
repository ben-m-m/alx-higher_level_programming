#!/usr/bin/python3
"""reading module"""


def read_file(filename=""):
    """reads and prints txt file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
