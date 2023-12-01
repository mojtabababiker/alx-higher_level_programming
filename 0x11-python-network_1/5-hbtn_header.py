#!/usr/bin/python3
""" print the header of a request using requests package """
import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id", None))
