#!/usr/bin/python3
def best_score(a_dictionary):
    list1 = []
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        val = a_dictionary.get(k)
        list1 += [val]
    large = list1[0]
    for i in list1:
        if i > large:
            large = i
    for k, v in a_dictionary.items():
        val1 = a_dictionary.get(k)
        if val1 == large:
            n = k
    return n
