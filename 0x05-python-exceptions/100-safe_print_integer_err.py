#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=stderr)
        return False
    return True
