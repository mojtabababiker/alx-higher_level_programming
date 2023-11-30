#!/bin/bash
# Bash script that send a HEAD request to URL using curl
curl -sI "$1" | grep "Content-Length" | awk -F ": " '{ print($2) }'
