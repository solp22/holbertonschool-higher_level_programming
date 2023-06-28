#!/usr/bin/python3
"""define class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation in a file"""
        if list_objs is None:
            lst = []
        else:
            lst = []
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """convert to python"""
        if json_string is None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        dummy = cls(5, 5)
        dummy.update(**dictionary)
        return dummy
