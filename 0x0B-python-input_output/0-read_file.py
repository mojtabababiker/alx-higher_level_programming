#!/usr/bin/python3
"""
Contains the read_file(filename="") function
"""


def read_file(filename=""):
    """
    Syntax:
        read_file(filename="")

    Description:
        Reads the text file `filename` using the `utf-8` decoding
        and prints  it to the stdout
    """

    with open(filename, 'r', encoding='utf-8') as fh:
        print(fh.read())
