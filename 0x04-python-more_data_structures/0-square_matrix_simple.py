#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Computs the square value of all integersof matrix.

    Args:
        matrix - 2D array
    Return:
        new_matrix with same size of matrix
    '''
    if matrix is None:
        return
    new_list = [[x ** 2 for x in row] for row in matrix]
    return new_list
