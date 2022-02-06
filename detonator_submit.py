#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print("Usage: python3 detonator_submit.py <file>")
    quit()

headers = {'API-KEY': 'xxx'}
post_data = {
    "public": 1 # Defines whether the submitted sample is sharable (1) or not (0)
}
response = requests.post('https://xxx.abuse.ch/api/submit/', data=post_data, files={'file': open(file,'rb')}, headers=headers)

print(response.content.decode("utf-8", "ignore"))
