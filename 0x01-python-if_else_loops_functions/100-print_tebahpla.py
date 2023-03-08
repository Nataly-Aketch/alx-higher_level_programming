#!/usr/bin/python3
for w in range(122, 96, -1):
    print(chr(w - 32) if w % 2 != 0 else chr(w), end="")
