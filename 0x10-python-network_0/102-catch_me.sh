#!/bin/bash
# Bash script inject message to be printed on the response body
curl -X "PUT" --location-trusted -u "user_id = 98":98 -Ls "0.0.0.0:5000/catch_me"
