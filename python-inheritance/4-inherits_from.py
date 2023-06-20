#!/usr/bin/python3
"""define is_same_class"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited
    from the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
