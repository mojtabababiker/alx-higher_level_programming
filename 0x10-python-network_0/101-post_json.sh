#!/bin/bash
# Bash script POST a json from a file to the server using curl
curl -d @"$2" -H "Content-Type: application/json" -X "POST" -s "$1"
