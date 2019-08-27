#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    request_id = result.headers.get("X-Request-Id")
    print(request_id)
