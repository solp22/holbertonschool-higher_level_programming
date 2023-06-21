#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line)
