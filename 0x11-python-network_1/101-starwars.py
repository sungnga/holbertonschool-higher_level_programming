#!/usr/bin/python3
"""A Python script that takes in a string and sends a search request to the
Star Wars API"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get('https://swapi.co/api/people/?search={}'
                            .format(sys.argv[1]))
    j_dict = response.json()
    print("Number of results: {}".format(j_dict['count']))
    for i in j_dict['results']:
        print(i['name'])
    while j_dict['next']:
        resp_next = requests.get(j_dict['next'])
        dict_next = resp_next.json()
        for i in dict_next['results']:
            print(i['name'])
    print('No result')
