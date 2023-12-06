#!/usr/bin/python3
def no_c(my_string):
    lst = []
    for i in my_string:
        if (i == 'c') or (i == 'C'):
            continue
        lst.append(i)
    s = ''.join(lst)
    return s
