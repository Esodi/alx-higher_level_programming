#!/bin/bash
# Bash script that sends a DELETE request to the URL.
curl -X DELETE -i http://"$1" | sed '1,/^\r\{0,1\}$/d'
