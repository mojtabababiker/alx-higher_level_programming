#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
        print a list elemnts in reversed oreder

        Args:
            my_list - list of number that will be printed from
    '''
    i = 0
    length = len(my_list)

    while i < length:
        print("{:d}".format(my_list[length - i - 1]))
        i += 1
