#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers."""
    lst = sorted(list_of_integers)
    if len(lst) != 0:
        return lst[-1]
    else:
        return None
