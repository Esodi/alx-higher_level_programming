#!/usr/bin/python3

""" This module contains the function to add two numbers.

"""


def add_integer(a, b=98):
    """ The function to add two integers """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
