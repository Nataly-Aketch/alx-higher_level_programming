#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for r in matrix:
        matrix2 = []
        for c in range(len(r)):
            matrix2 += [r[c] ** 2]
        matrix1 += [matrix2]
    return matrix1
