#!/usr/bin/python3

"""module with a function"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
