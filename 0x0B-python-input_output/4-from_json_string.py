#!/usr/bin/python3
"""
contains the from_json_string(my_str) function
"""
import json


def from_json_string(my_str):
    """
    Syntax:
        from_json_string(my_str)

    Description:
        Convret a json string to python object and return
        this representation
    """

    return json.loads(my_str)
