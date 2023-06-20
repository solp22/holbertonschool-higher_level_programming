#!/usr/bin/python3
"""define is_same_class"""
def is_same_class(obj, a_class):
    """eturns True if the object is exactly an instance of
    the specified class; otherwise False"""
    return isinstance(obj, a_class)
