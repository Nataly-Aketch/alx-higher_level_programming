#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        len1 = len(row)
        for i in range(len1):
            print("{:d}".format(row[i]), end=" ")
        print()
