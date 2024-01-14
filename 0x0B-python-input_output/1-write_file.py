#!/usr/bin/python3

"""a module with file operations in py"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
