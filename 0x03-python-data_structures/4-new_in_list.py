#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    lst = list(my_list)
    if (idx < 0) or (idx > len(lst) - 1):
        return (lst)
    lst[idx] = element
    return (lst)
