#!/usr/bin/python3
"""
script that takes in a URL, sends a request
to the URL and displays the body of the response
"""

import urllib.request
from sys import argv
import urllib.error

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
