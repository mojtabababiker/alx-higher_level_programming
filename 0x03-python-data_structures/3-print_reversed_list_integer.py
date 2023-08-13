#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
        print a list elemnts in reversed oreder

        Args:
            my_list - list of number that will be printed from
    '''

    i = len(my_list) - 1
    if i < 0:
        print()
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
