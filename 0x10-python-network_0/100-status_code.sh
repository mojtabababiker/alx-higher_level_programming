#!/bin/bash
# Bash script that prints a request status code using curl
curl -w '%{http_code}' -o "test.txt" -s "$1"
