#!/usr/bin/python3
"""define class"""


class MyList(list):
    """class Mylist that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
