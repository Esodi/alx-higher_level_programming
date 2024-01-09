#!/usr/bin/python3

"""
    MOdule that contain a function that divides elements of a matrix.

"""


def matrix_divided(matrix, div):
    """ The function that divides all elements of ta matrix """

    k = []
    stry = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    x = len(matrix[0])
    k = [list(s) for s in matrix]
    for i in k:
        if len(i) != x:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(i)):
            if not isinstance(i[j], (int, float)):
                raise TypeError(stry)
            i[j] = round((i[j] / div), 2)
    return k
