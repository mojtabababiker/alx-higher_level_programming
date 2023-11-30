#!/bin/bash
# Bash script that send a HEAD request to URL using curl
curl -sI 0.0.0.0:5000 | grep "Content-Length" | awk -F ": " '{ print($2) }'
