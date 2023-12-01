#!/usr/bin/python3
""" get X-request-id from headers """
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])