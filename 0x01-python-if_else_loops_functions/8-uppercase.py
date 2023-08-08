#!/usr/bin/python3
def uppercase(st):
    str_len = len(st)
    char = 0
    printed_char = " "
    if str_len == 0:
        return
    while char < str_len:
        if st[char] >= 'a' and st[char] <= 'z':
            printed_char = chr((ord(st[char]) - 32))
        else:
            printed_char = st[char]
        print(printed_char, end='')
        char += 1
    print()
