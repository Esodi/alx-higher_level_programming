#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers."""
    lst = list_of_integers.sort()
    return lst[0]
