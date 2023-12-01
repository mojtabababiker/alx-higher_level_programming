#!/bin/bash
# Bash script that displays all HTTP methods the server will accept
curl -I -s "$1" | grep "Allow" | awk -F ": " '{ print($2) }'
