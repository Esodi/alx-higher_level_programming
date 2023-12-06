#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst = list(my_list)
    if (idx < 0) or (idx > len(lst)):
        return (lst)
    lst[idx] = element
    return (lst)
