#!/usr/bin/python3
'''Matrix divided module'''


def matrix_divided(matrix, div):
    '''divide a matrix by div'''
    result = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for elements in matrix:
        if type(elements) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for i in elements:
            if type(i) != int and type(i) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    "of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for lst in matrix:
        result.append(list(map(lambda x: round(x / div, 2), lst)))
    return result
