#!/usr/bin/python3
""" sending a request to a server and handling the http or the url error """
import sys
import urllib.request
import urllib.error


try:
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        print(str(res.read()))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
