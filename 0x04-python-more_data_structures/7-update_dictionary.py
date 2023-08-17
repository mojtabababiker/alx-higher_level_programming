#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''
    replace or add key/value in a dictionary

    Args:
        a_dictionary - a dictionary to be updated
        key - the new or exsisting key name
        value - the value to be added to the key

    Return:
        new updated dictionary
    '''

    for kee in a_dictionary.keys():
        if kee == key:
            a_dictionary[kee] = value
            return a_dictionary
    a_dictionary.setdefault(key, value)

    return a_dictionary
