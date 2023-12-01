#!/bin/bash
# Bash script that sends POST request and prints the body using curl
curl -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -s "$1"
