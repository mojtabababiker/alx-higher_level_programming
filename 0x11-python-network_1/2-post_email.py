#!/usr/bin/python3
""" send an email using urllib.request module """
import sys
import urllib.request
import urllib.parse

email = {"email": sys.argv[2]}
email = urllib.parse.urlencode(email)
req = urllib.request.Request(sys.argv[1], email)
with urllib.request.urlopen(req) as res:
    print(str(res.read()))
