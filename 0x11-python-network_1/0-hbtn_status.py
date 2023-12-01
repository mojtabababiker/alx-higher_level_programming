#!/usr/bin/python3
"""fetch server using urllib package"""
if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(str(content)))
