#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print('{}'.format(''))
    for i in matrix:
        if i is None:
            print('')
        for j in range(0, len(i)):
            if j < len(i) - 1:
                print("{:d}".format(i[j]), end=' ')
            else:
                print("{:d}".format(i[j]))
