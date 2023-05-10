#!/usr/bin/python3

def uppercase(str):
    c = ''
    for i in str:
        c = i
        if (i >= 'a' and i <= 'z'):
            c = ord(i) - 32
        print("%c" %c, end='')
    print("%c" %10, end='')
