#!/usr/bin/python3
"""
Contains the write_file(filename="", text="") function
"""


def write_file(filename="", text=""):
    """
    Syntax:
        write_file(filename="", text="")

    Description:
        Write the `text` string to the the text file `filename`
        using the `utf-8` encoding
    """

    with open(filename, "w", encoding="utf-8") as fh:
        chars_num = fh.write(text)
    return chars_num
