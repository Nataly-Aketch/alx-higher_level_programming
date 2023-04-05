#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix matrix with div.
    args:
        matrix - matrix to be divided
        div - divisor
    returns a new matrix
    Raises exceptions"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if div != div or div == float('inf') or div == -float('inf'):
        div = 10
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(isinstance(item, list) for item in matrix):
        raise TypeError(err)
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for i in range(len(row)):
            if not isinstance(row[i], (int, float)):
                raise TypeError(err)
    return [[round(item / div, 2) for item in row] for row in matrix]
