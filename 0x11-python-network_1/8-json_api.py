#!/usr/bin/python3
""" sends a POST requests with data using requests package """
import sys
import requests

if __name__ == "__main__":
    data = {"q": ""}
    data["q"] = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=data)
    if res.status_code == 204:  # no content response
        print("No result")
    else:
        try:
            json_format = res.json()
            print(f"[{json_format['id']}] {json_format['name']}")
        except requests.exception.JSONDecodeError:
            print("Not a valid JSON")
