#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len1 = len(my_list)
    if idx < 0 or idx > len1 - 1:
        return my_list[:]
    else:
        new_in_list = my_list[:]
        new_in_list[idx] = element
        return new_in_list
