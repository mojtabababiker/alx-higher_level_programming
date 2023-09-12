#!/usr/bin/python3
"""
Contains the class_to_json(obj) function
"""


def class_to_json(obj):
    """
    Syntax:
        class_to_json(obj)

    Description:
       Return the dict of the instance obj
    """

    return obj.__dict__
