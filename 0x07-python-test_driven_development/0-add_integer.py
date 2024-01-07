#!/usr/bin/python3

""" This module contains the function to add two numbers.

"""


def add_integer(a, b=98):
    """ The function to add two integers """

    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
