#!/usr/bin/python3
"""
gets the last 10 commits
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(comit.get("commit").get('author').get('name'))
