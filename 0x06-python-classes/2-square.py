#!/usr/bin/python3
"""A module created for square class.

"""


class Square:
    """A class contains Square attributes.

    """
    def __init__(self, size=0):
        """A method that initialize class.
           Args:
                size (int): int value.

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
