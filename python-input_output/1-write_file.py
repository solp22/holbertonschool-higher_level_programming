#!/usr/bin/python3
"""define write_file function"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
