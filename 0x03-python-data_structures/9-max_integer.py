#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    v = 0
    for i in my_list:
        if i > v:
            v = i
    return v
