#!/usr/bin/python3
"""
This module contains only one function:
    say_my_name(first_name, last_name="")
"""

def say_my_name(first_name, last_name=""):
    """
    say_my_name takes two strings first name and last name, and
    prints `My name is <first_name> <last_name>`

    Args:
        first_name: string of the first name
        last_name: string of the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

