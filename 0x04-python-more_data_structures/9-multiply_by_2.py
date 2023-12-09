#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = dict(a_dictionary)
    for k in d.keys():
        d[k] = 2 * d[k]
    return d
