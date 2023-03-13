#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len1 = len(matrix)
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end=" ")
        print()
