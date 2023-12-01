#!/usr/bin/python3
""" sends a POST requests with data using requests package """
import sys
import requests

if __name__ == "__main__":
    data = {'q': ''}
    data['q'] = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    try:
        res = requests.post(url, data=data)
        res.raise_for_status()

        json_format = res.json()
        print(f"[{json_format['id']}] {json_format['name']}")

    except requests.exceptions.HTTPError:
        print("Not a valid JSON")

    except KeyError:
        print("No result")
