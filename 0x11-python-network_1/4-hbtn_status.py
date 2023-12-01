#!/usr/bin/python3
""" using request package to make http request to a server """
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    content = res.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
