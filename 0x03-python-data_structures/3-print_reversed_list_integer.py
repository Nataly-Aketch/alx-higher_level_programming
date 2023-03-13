#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    list_copy = my_list[::-1]
    for i in list_copy:
        print("{:d}".format(i))
