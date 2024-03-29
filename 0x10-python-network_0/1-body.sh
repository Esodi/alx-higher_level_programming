#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body.
curl -si "$1" -o dev/null -w "%{http_code}" | grep -q "200" && curl -s http://"$1"
