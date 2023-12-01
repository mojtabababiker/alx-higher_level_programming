#!/usr/bin/python3
""" posting by using the requests package """
import sys
import requests

res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
print(res.text)
