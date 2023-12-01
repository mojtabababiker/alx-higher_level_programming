#!/usr/bin/python3
""" print the header of a request using requests package """
import sys
import requests


res = requests.get(sys.argv[1])
print(res.headers.get("X-Request-Id", None))
