#!/usr/bin/python3
""" get a GitHub user id using GitHub API """
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               }

    try:
        res = requests.get(url, headers=headers,
                           auth=(sys.argv[1],
                                 sys.argv[2]),
                           )
        res.raise_for_status()

        print(res.json())

    except (requests.exceptions.HTTPError, KeyError):
        print("None")
