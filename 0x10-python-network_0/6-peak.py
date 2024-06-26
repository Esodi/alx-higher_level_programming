#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers."""
    list_of_integers.sort()
    if len(list_of_integers) != 0:
        return list_of_integers[-1]
    return None
