#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    adds two tuples together

    Args:
        tuple_a - first tuple
        tuple_b - second tuble
    Return:
        A tuple of the form (add the first elements, add the second elements)
    '''
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    elif len_a == 0:
        a1 = 0
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = 0

    if len_b >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    elif len_b == 0:
        b1 = 0
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = 0
    return (a1 + b1, a2 + b2)
