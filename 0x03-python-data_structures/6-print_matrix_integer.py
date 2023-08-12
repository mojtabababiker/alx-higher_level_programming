#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''
        prints 2D List

        Args:
            matrix - 2D list to be print
    '''
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            end = ' '
            if col == len(matrix[row]) - 1:
                end = ''
            print("{:d}".format(matrix[row][col]), end=end)
        print()
