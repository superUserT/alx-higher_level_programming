#!/usr/bin/python3
""" get X-Request-ID using requests """
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])