#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
        Change element at index idx of my_list and return
        a new copy of this list

        Args:
            my_list - list to copy and changed
            idx - index of the element that will be changed
            element - the new element value
        Return:
            A copy of the list my_list either modified or not
            depending on if the idx is valid or not
    '''
    if (idx < 0 or idx >= len(my_list)):
        return (my_list[:])

    return ([num if not num == my_list[idx] else element for num in my_list])
