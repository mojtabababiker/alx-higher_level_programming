#!/usr/bin/python3
""" make a request to a server by using the equests
package and handle errors """
import sys
import requests

try:
    res = requests.get(sys.argv[1])
    print(res.text)
except requests.exceptions.HTTPError:
    print("Error code: {}".format(res.status_code))
