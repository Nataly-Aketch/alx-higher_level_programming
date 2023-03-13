#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len1 = len(matrix)
    if len1 > 1:
        for row in matrix:
            for i in range(len(row)):
                if i != len(row) - 1:
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]), end="\n")
    else:
        print()
        return
