#!/usr/bin/python3
def no_c(my_string):
    len1 = len(my_string)
    new_string = ''
    for i in range(len1):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_string = my_string[:i] + my_string[i + 1:]
    return new_string
