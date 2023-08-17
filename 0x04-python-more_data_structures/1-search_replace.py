#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    replace all occurrences of an element by another in a new list

    Args:
        my_list - the initial list
        search - is the element to replace in the list
        replace - is the new element

    Return:
        the new_list with the new element
    '''
    if my_list is None:
        return
    return [elmnt if elmnt != search else replace for elmnt in my_list]
