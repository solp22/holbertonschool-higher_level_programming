#!/usr/bin/python3
'''add_integer module'''


def add_integer(a, b=98):
    '''add integers'''
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
