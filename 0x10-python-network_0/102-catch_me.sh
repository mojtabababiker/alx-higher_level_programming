#!/bin/bash
# Bash script inject message to be printed on the response body
curl --location-trusted -d "user_id=98":98 -H "Origin: School" \
     -X "PUT" -Ls "0.0.0.0:5000/catch_me"
