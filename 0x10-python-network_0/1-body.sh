#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body.
curl -si -o response.txt -w "%{http_code}" "$1" && [ "$(cat response.txt)" = "200" ] && curl -s "$1"

