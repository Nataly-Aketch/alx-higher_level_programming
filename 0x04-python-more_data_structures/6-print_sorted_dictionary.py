#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    new_dict = dict(sorted_dict)
    for i, j in new_dict.items():
        print("{}: {}".format(i, j))
