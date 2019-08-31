#!/usr/bin/python3
"""A Python script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            auth=(sys.argv[1], sys.argv[2]))
    j_dict = response.json()
    try:
        print(j_dict['id'])
    except KeyError:
        print('None')
