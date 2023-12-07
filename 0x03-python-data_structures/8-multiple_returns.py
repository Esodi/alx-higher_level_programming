#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    j = len(sentence)
    if not sentence:
        tup = tup + (0, None,)
        return (tup)
    k = sentence[0]
    tup = tup + (j, k,)
    return tup
