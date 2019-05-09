#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for elem in row:
            return [[elem**2 for elem in row] for row in matrix]
        return matrix
