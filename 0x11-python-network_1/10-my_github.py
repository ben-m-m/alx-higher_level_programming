#!/usr/bin/python3
"""
takes github credentials and displays id using Github API
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(argv[1], argv[2])

    res = requests.get(url, auth=auth)
    print(res.json().get("id"))
