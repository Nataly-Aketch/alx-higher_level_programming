#!/usr/bin/python3
def uppercase(str):
    for w in str:
        o = ord(w)
        if o >= 97 and o <= 122:
            w = chr(ord(w) - 32)
        else:
            w = chr(ord(w))
        print("{}".format(w), end="")
    print(end='\n')
