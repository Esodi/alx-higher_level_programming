#!/usr/bin/python3

"""a module with python file operations"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""

    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
