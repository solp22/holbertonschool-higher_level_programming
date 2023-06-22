#!/usr/bin/python3
"""define save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    json_obj = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json_obj)
