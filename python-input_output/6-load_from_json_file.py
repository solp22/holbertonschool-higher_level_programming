#!/usr/bin/python3
"""define load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an object(python) from a json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        json.loads(f.read())
