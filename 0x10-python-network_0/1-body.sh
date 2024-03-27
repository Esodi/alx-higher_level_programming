#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body.
curl -s -o /dev/null -w "%{http_code}" http://"$1" | grep -q 200 && curl -s http://"$1"
