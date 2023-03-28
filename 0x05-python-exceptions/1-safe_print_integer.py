#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        j = True
    except ValueError:
        j = False
    except TypeError:
        j = False
    return j
