#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body.
curl -sI http://"$1" | grep -q 200 && curl -s http://"$1"
