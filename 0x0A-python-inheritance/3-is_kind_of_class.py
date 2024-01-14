#!/usr/bin/python3

"""a module performing instance checking"""


def is_kind_of_class(obj, a_class):
    """a function checking type of an instance"""

    if isinstance(obj, a_class):
        return True
    return False
