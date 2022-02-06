#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print("Usage: python3 detonator_submit.py <file>")
    quit()

headers = {'API-KEY': 'xxx'}
response = requests.post('https://xxx.abuse.ch/api/submit/', files={'file': open(file,'rb')}, headers=headers)

print(response.content.decode("utf-8", "ignore"))
