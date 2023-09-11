#!/usr/bin/python3
"""
Contains the is_kind_of_class(obj, a_class) function
"""


def is_kind_of_class(obj, a_class):
    """
    Syntax:
        is_kind_of_class(obj, a_class)

    Description:
        Check the obj if its an instance of the class a_class or
        a subclass of it and return True, otherwise False will be
        returned.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
