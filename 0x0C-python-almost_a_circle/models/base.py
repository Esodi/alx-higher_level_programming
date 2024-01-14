#!/usr/bin/python3
"""a module with base class opearations"""


class Base:
    """a class with base operations"""

    __nb_objects = 0

    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
