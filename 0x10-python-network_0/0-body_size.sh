#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays size.
curl -s http://"$1" | wc -c
