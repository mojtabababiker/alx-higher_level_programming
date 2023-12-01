#!/bin/bash
# Bash script that send GET request with header variable and prints its body
curl -H "X-School-User-Id: 98" -s "$1"
