#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    if len1 == 0:
        tuple1 = (len1, None)
    else:
        tuple1 = (len1, sentence[0])
    return tuple1
