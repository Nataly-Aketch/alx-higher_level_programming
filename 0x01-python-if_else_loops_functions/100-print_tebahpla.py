#!/usr/bin/python3
for w in range(122, 96, -1):
    if w % 2 != 0:
        print(chr(w - 32), end="")
    else:
        print(chr(w), end="")
