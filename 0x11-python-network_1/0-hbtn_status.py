#!/usr/bin/python3
"""
script that fetches url
"""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    res = response.read()

print('Body response:')
print('\t- type:', type(res))
print('\t- content:', res)
print('\t- utf8 content:', res.decode('utf-8'))
