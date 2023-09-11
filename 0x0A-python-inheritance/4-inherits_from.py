#!/usr/bin/python3
"""
Contains the inherits_from(obj, a_class) function
"""


def inherits_from(obj, a_class):
    """
    Syntax:
        inherits_from(obj, a_class)
    Description:
        Check the obj if its  instance of a supclass of the
        a_class and return True, otherwise False will be
        returned.
    """

    return isinstance(obj, a_class) and not (type(obj) is a_class)


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
