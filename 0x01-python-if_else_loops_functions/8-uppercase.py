#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if (i >= 'a' and i <= 'z'):
            i = ord(i) - 32
        print("%c" %i, end='')
    print("")
