#!/usr/bin/python3
"""my list sorting module"""


class MyList(list):
    """sub-class of list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
