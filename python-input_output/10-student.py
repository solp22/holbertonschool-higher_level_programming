#!/usr/bin/python3
"""define class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(self, Student):
            if attrs is None:
                return self.__dict__
        dict = {}
        for element in attrs:
            if element in self.__dict__.keys():
                dict[element] = self.__dict__[element]
        return dict
