#!/usr/bin/python3

""" Module with list inhereted """


class MyList(list):
    """a class that inherit from list"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        s = sorted(self)
        print(s)
