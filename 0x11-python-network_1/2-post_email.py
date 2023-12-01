#!/usr/bin/python3
""" send an email using urllib.request module """
import sys
import urllib.request, urllib.parse

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    email = urllib.parse.urlencode(email)
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
