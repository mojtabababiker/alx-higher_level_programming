#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''
    Function that prints a list of integer, each number in a diffrent line

    Args:
        my_list - list of integers
    '''
    for num in my_list:
        print("{:d}".format(num))
