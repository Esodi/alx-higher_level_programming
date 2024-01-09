#!/usr/bin/python3

"""
    module that contain function for text indentation.

"""


def text_indentation(text):
    """prints a 2 new lines after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == ':' or i == '?':
            print(i)
            print()
        else:
            print(i, end='')
