#!/usr/bin/python3
"""
Contains the save_to_json_file(my_obj, filename) function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Syntax:
        save_to_json_file(my_obj, filename)

    Description:
        Write the Json representation of the my_obj and write it
        to the file filename, if the file isn't created this
        function will create it
    """

    with open(filename, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(my_obj))
