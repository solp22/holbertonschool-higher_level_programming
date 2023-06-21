#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """open file and print to stdout"""
    with open(filename, mode='r', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
