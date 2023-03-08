#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i != j and j > i and i != 8:
            print("{}{}".format(i, j), end=", ")
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
