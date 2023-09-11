#!/usr/bin/python3
"""
0-lookup is contains one function:
lookup(obj)
"""


def lookup(obj):
    """
    Usage:
        lookup(obj)

    Description:
        Get an obkect as arguments and return a list of all its attributes
        and methods.
    """

    return list(obj.__dict__)
