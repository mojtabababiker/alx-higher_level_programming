#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''
    function that returns a set of common elemnts in two sets

    Args:
        set_1 - the first set
        set_2 - the second set

    Return:
        a new set of common elemnts in the two set if there is ones,
        or empty set otherwise
    '''
    return set_1.intersection(set_2)
