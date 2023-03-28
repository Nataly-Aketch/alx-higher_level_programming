#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        j = True
    except (ValueError, TypeError) as ex:
        print("Exception: ", ex, file=sys.stderr)
        j = False
    return j
