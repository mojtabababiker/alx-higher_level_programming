#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    Function that retrieves an element from a list like in `C`

    Args:
        my_list - list of item to retrieve an element from it
        idx - the index of the required item
    Return:
        The retrieved item if one, or None otherwise
    '''
    if idx < 0 or idx >= len(my_list):
        return (None)
    return (my_list[idx])
