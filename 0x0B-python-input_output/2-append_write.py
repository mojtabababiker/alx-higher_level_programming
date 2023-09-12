#!/usr/bin/python3
"""
Contains the append_file(filename="", text="") function
"""


def append_file(filename="", text=""):
    """
    Syntax:
        append_file(filename="", text="")

    Description:
        Write the `text` string to the the text file `filename`
        using the `utf-8` encoding
    """

    with open(filename, "a", encoding="utf-8") as fh:
        chars_num = fh.write(text)
    return chars_num
