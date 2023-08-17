#!/usr/bin/python3
def merg(left: list, right: list, key_list: list) -> list:
    '''
    merge two list together in alphabeticly ordere

    Args:
        left - the first list
        right - the second list
        key_list - the list to sort

    Return:
        a sorted key_list
    '''
    lft = 0  # for the left side of the list
    rght = 0  # for the right side of the list
    k = 0  # for the key_list

    while lft < len(left) and rght < len(right):
        if left[lft][0] <= right[rght][0]:
            key_list[k] = left[lft]
            lft += 1
        else:
            key_list[k] = right[rght]
            rght += 1
        k += 1

    while lft < len(left):
        key_list[k] = left[lft]
        k += 1
        lft += 1

    while rght < len(right):
        key_list[k] = right[rght]
        k += 1
        rght += 1

    return (key_list)


def sort_key(key_list: list) -> list:
    '''
    sort a given list alphabeticly, and return a new list

    Args:
    key_list - list of strings

    Return:
        new sorted list
    '''
    if len(key_list) == 1:
        return key_list

    left = sort_key(key_list[:len(key_list) // 2])
    right = sort_key(key_list[len(key_list) // 2:])

    return merg(left, right, key_list)


def print_sorted_dictionary(a_dictionary):
    '''
    Print a dictionary by ordered kkeys

    Args:
        a_dictionary - a dictionary to ordered and print it
    '''

    if a_dictionary is None:
        return
    key_list = [key for key in a_dictionary.keys()]
    if len(key_list) == 0:
        return

    key_list = sort_key(key_list)
    for key in key_list:
        print("{}: {}".format(key, a_dictionary[key]))
