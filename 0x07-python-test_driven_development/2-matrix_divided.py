#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix matrix with div.
    args:
        matrix - matrix to be divided
        div - divisor
    returns a new matrix
    Raises exceptions"""
    if div == 0:
        raise ZeroDivisionError("division by 0")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(isinstance(item, list) for item in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    new = []
    for row in matrix:
        for i in range(len(row)):
            if not isinstance(row[i], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = row[i] / div
            new.append(round(result, 2))
    len1 = len(row)
    res = [new[0:len1]] + [new[len1:]]
    return res