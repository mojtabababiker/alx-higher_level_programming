#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
    find all the multiples by 2 in my_list

    Args:
        my_list - list of integers
    Return:
        A new list with `True` or `False` depending on whether the ineger at
            the same postion is multiple of 2
    '''
    return [True if num % 2 == 0 else False for num in my_list]
