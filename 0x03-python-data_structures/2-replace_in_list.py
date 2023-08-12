#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    Function that replaces an element of a list at a specific position
    (like in C).

    Args:
        my_list - List of elements to replace an item on it
        idx - the index of the item that will be replaced
        element - the new element thet will replaced with
    Return:
        A new modified list, or the original list if the idx is not in rang
        of my_list
    '''
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
