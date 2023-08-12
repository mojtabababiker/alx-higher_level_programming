#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
        print a list elemnts in reversed oreder

        Args:
            my_list - list of number that will be printed from
    '''
    list_len = len(my_list) - 1
    for i in range(list_len, -1, -1):
        print("{:d}".format(my_list[i]))
