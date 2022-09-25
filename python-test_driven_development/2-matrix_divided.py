#!/usr/bin/python3
'''
The "2-matrix_divided" with function:

matrix_divided(matrix, div)
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix and returns the result.'''
    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_len = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        row_len.append(len(row))
        if not all(element_len == row_len[0] for element_len in row_len):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(number / div, 2) for number in row] for row in matrix]
