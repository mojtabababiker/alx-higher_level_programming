#!/usr/bin/python3
"""
This module contians only one function
print_square(size)
"""


def print_square(size):
    """
    print_square(size)
    print a square using the `#` symbol
    with the `size` size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end='')
        if i != size - 1:
            print()
    print()
