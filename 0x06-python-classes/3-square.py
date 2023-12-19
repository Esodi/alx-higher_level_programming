#!/usr/bin/python3
"""A module that finds an area of a square

"""


class Square:
    """A class that contain squae attributes.

    """
    def __init__(self, size=0):
        """initialization method.

        """
        if size < 0:
            raise ValueError('size must be >= 0')
        elif not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            self.__size = size

    def area(self):
        """A method that calculate the area of the square.

        """
        return self.__size ** 2
