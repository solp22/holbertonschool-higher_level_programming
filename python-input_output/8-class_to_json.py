#!/usr/bin/python3
"""define class_to_json function"""


def class_to_json(obj):
    """convert a class to json"""
    return obj.__dict__
