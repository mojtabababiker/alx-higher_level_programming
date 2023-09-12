#!/usr/bin/python3
"""
Contains the load_from_json_file(filename) funcrion
"""
import json


def load_from_json_file(filename):
    """
    Syntax:
        load_from_json_file(filename)

    Description:
        Creat and return python object from the json representation
        that is in the file filename
    """

    with open(filename, "r", encoding="utf-8") as fh:
        return json.loads(fh.read())
