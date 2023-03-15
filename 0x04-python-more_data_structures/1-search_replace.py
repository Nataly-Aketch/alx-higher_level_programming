#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    new_list = list(map(lambda i: replace if i == search else i, my_list))
    '''for i in my_list:
        if i == search:
            i = replace
        new_list += [i]'''
    return new_list
