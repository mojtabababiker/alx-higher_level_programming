#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
    Find the bigest integer of a list

    Args:
        my_list - list of integers
    Retunr:
        The max number in the list, or None if the list is empty
    '''
    lenght = len(my_list)
    if lenght == 0:
        return None
    my_list.sort()
    return (my_list[-1])
