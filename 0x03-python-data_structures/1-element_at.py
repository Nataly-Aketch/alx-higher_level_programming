#!/usr/bin/python3
def element_at(my_list, idx):
    len1 = len(my_list)
    if idx < 0 or idx > len1 - 1:
        return None
    return my_list.pop(idx)
