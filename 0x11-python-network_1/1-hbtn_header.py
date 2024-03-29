#!/usr/bin/python3
""" retrive a cerian header value from a request with urllib """

if __name__ == "__main__":
    import sys
    import urllib.request

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        print(res.headers.get("X-Request-Id", None))
