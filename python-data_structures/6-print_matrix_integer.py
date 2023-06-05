#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for val in range(len(matrix[row])):
                if (val < len(matrix[row]) - 1):
                    print("{:d}".format(val), end=" ")
                else:
                    print("{:d}".format(val), end="")
            print()
