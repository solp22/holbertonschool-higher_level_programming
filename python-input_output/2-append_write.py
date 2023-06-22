#!/usr/bin/python3
"""define append_write function"""


def append_write(filename="", text=""):
    """append text into file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
