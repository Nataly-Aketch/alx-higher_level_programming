#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    sum1 = 0
    for i in set1:
        sum1 += i
    return sum1
