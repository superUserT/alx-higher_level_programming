#!/usr/bin/python3
""" json api """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})
    response_data = response.json()

    try:
        if response_data:
            print("[{}] {}".format(response_data['id'], response_data['name']))
        elif not response_data:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")