#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list[:]
    for i in newlist:
        if i % 2 == 0:
            newlist[i] = 1
        else:
            newlist[i] = 0
    return newlist
