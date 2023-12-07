#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst = []
    for i in range(2):
        if i < len(tuple_a):
            v_a = tuple_a[i]
        else:
            v_a = 0
        if i < len(tuple_b):
            v_b = tuple_b[i]
        else:
            v_b = 0
        sum_t = v_a + v_b
        lst.append(sum_t)
    t = tuple(lst)
    return t
