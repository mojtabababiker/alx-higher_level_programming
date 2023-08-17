#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
    delete a key in dictionary

    Args:
        a_dictionary - dictionary to delete a key from it
        key - the key to be deleted

    Return:
        a dictionary without the key
    '''
    if key not in a_dictionary.keys():
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
