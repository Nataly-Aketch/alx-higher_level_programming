#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len1 = len(my_list) - 1
    if len1 > 0:
        for i in my_list[::-1]:
            print("{:d}".format(i))
