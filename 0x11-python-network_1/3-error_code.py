#!/usr/bin/python3
""" sending a request to a server and handling the http or the url error """
import sys
import urllib.request, urllib.error

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
