#!/usr/bin/python3
import json
"""define class"""


class Base:
    """initialize class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)