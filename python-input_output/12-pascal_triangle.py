#!/usr/bin/python3
"""define the pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n"""
    triangle = [[1]]
    for tri in range(n - 1):
        new = []
        for lst in range(len(triangle[tri]) + 1):
            if lst == 0 or lst == len(triangle[tri]):
                new.append(1)
            else:
                new.append(triangle[tri][lst - 1] + triangle[tri][lst])
        triangle.append(new)
    if n <= 0:
        return [[]]
    return triangle
