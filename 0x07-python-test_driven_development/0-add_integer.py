#!/usr/bin/python3
"""
This Module only contains one function

     add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    add_integer(a, b=98)
    [=] Add two integer and returns the result
    [=] Raises a TypeError if `a` or `b` is not an integer or float

    Args:

        a: first number
        b: second numbeer, with default value `98`

    Return:

        a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a + b)
