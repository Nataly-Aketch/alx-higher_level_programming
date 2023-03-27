#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        j = 1
    except ValueError:
        j = 0
    return j
