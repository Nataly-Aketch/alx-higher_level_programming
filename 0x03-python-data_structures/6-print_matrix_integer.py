#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len1 = len(matrix)
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=" ")
        print()
