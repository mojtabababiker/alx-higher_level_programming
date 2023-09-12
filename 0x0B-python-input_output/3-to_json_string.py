#!/usr/bin/python3
"""
contains the to_json_string(my_obj) function
"""
import json


def to_json_string(my_obj):
    """
    Syntax:
        to_json_string(my_obj)

    Description:
        Convret a python object to a json string and return
        this representation
    """

    return json.dumps(my_obj)
