#!/usr/bin/python3
"""define save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """write json convertion in a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
