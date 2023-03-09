#!/usr/bin/python3
import sys
len1 = len(sys.argv)
sum = 0
for i in range(1, len1):
    sum += int(sys.argv[i])
if __name__ == "__main__":
    print("{}".format(sum))
