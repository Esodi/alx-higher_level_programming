#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d '{"email": "test@gmail.com"}' http://"$1"
