#!/usr/bin/python3
"""A Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally displays
the body of the response"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
