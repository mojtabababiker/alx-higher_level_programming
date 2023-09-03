#!/usr/bin/python3
"""
This module contians only one function

   matrix_divided(matrix, div)
"""

def matrix_divided(matrix, div):
    """
    matrix_divided takse a list of lists that have the same length
    divides each elements on this list by the div arg.
    and return new matrix of the results

    matrix_divided(matrix, div)

    Args:
        matrix: a list of integer/float lists with the same length
        div: integer or float number to divide py

    Return:
        A new matrix with the result

    """
    new_matrix = []
    temp = []
    i = 0
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    while i < len(matrix) - 1:
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1
    for row in matrix:
        for val in row:
            if type(val) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)" +
                " of integers/floats")
            temp.append(round(val / div, 2))
        new_matrix.append(temp)
        temp = []

    return new_matrix
