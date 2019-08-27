#!/usr/bin/python3
"""A Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally displays
the body of the response"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post(sys.argv[1], data={'q': q})
    try:
        j_dict = response.json()
        if j_dict:
            print('[{}] {}'.format(j_dict.get('id'), j_dict.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
