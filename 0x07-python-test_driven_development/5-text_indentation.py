#!/usr/bin/python3
"""
This module contains only one function
text_indentation(text)
"""


def text_indentation(text):
    """
    text_indentation takse one argument `text`, in which it
         will prints a new line after each `.` ,`?` and `:`

    Args:
        text: a string letral containing the text
    """
    text_len = len(text)
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < text_len:
        print(text[i], end='')
        if text[i] in [".", ":", "?"]:
            print("\n")
            if i != text_len - 1:
                if text[i + 1] == " ":
                    i += 1
        i += 1
