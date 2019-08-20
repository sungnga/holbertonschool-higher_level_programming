#!/bin/bash
# A Bash script that sends a DELETE request to the URL \
passed as the first argument and displays the body of t\
he response
curl -sX DELETE $1
