#!/usr/bin/python3
""" send an email using urllib.request module """
import sys
from urllib import request, parse

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    email = parse.urlencode(email)
    email = email.encode("ascii")
    req = request.Request(sys.argv[1], email)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
