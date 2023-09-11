#!/usr/bin/python3
"""
Contains the is_same_class(obj, a_class) function
"""


def is_same_class(obj, a_class):
    """
    Syntax:
        is_same_class(obj, a_class)

    Description:
        Check the obj if its exactly an instance of the class
        a_class and return True, otherwise False will be
        returned.

    Args:
        obj: an python object
        a_class: the python class to check
    """

    return type(obj) is a_class


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
