#!/usr/bin/python3
def number_keys(a_dictionary):
    '''
    calculate and return the number of keys in a dictionary

    Args:
        a_dictionary - a dictionary to calculate its keys

    Return:
        number of keys
    '''
    number_keys = 0
    for key in a_dictionary.keys():
        number_keys += 1
    return number_keys
