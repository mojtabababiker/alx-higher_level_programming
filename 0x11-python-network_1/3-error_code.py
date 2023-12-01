#!/usr/bin/python3
""" sending a request to a server and handling the http or the url error """
import sys
from urllib import error, request

if __name__ == "__main__":
    try:
        req = request.Request(sys.argv[1])
        with request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
