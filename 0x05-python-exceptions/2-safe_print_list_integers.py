#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    d, c = (0, 0)
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end='')
                c += 1
            d += 1
        print()
    except IndexError:
        pass
    if x > d:
        raise IndexError('list index out of range')
    return c
