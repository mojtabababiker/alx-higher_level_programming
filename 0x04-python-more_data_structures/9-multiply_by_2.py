#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''
    multibly all values in a_dictionary by 2 and return a
    new dictionary of these values

    Args:
        a_dictionary - the source dictionary

    Return:;
        a new dictionary of the new values
    '''
    new_dict = dict()
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
