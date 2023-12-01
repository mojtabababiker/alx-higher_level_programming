#!/usr/bin/python3
""" get a GitHub user id using GitHub API """
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"
               }

    data = {"access_token": sys.argv[2]}
    try:
        res = requests.post(url, headers=headers, data=data,
                            auth=(sys.argv[1], sys.argv[2]))
        print(res.json()["id"])

    except (requests.exceptions.HTTPError, KeyError):
        print("None")
