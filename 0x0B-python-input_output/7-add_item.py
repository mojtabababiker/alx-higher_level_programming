#!/usr/bin/python3
"""
This is a script wich takes alll the command line arguments and add
them to python list then save them to .json file
"""
import json
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """
    Code entry point for the program
    """

    try:
        args = load_from_json_file("add_item.json")
    except Exception as e:
        args = []
    for i in range(1, len(sys.argv)):
        args.append(sys.argv[i])
    save_to_json_file(args, "add_item.json")


if __name__ == "__main__":
    main()
