#!/usr/bin/python3
"""deifne from_json_string function"""
import json


def from_json_string(my_str):
    """convert from json to python"""
    return json.loads(my_str)
