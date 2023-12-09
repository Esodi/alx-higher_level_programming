#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    h = -1024
    for k in a_dictionary:
        if a_dictionary[k] > h:
            h = a_dictionary[k]
            n = k
    return n
