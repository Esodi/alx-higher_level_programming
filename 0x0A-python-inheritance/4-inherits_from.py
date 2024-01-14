#!/usr/bin/python3
"""a module with inherits_from() function"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
    #    """return True
   # else:
    #    return False"""
