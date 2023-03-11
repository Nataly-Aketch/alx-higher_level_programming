#!/usr/bin/python3
def max_integer(my_list=[]):
    len1 = len(my_list)
    if len1 == 0:
        return None
    large = my_list[0]
    for i in my_list:
        if i > large:
            large = i
    return large
