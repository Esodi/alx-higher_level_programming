#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ln = list(my_list)
    for i in range(len(my_list)):
        if ln[i] == search:
            ln[i] = replace
    return ln
