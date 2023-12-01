#!/usr/bin/python3
""" using request package to make http request to a server """
import requests

url = "https://alx-intranet.hbtn.io/status"
res = requests.get(url)
content = res.text
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
