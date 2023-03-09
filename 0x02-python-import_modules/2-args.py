#!/usr/bin/python3
import sys
len1 = len(sys.argv)
if __name__ == "__main__":
    if len1 == 1:
        print("{} arguments.".format(len1 - 1))
    else:
        if len1 == 2:
            print("{} argument:".format(len1 - 1))
        else:
            print("{} arguments:".format(len1 - 1))
        for w in range(1, len1):
            print("{:d}: {}".format(w, sys.argv[w]))
