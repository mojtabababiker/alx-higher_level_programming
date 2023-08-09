#!/usr/bin/python3
def uppercase(st):
    str_len = len(st)
    char = 0
    prnt_char = ""
#    if str_len == 0:
#        return
    while char < str_len:
        if st[char] >= 'a' and st[char] <= 'z':
            prnt_char = chr((ord(st[char]) - 32))
        else:
            prnt_char = st[char]
        print("{}".format(prnt_char, 'c'), end='')
        char += 1
    print("{}".format(""))


"""uppercase("test one")
uppercase("test_two")
uppercase("test3")
uppercase("test4 'four'")
uppercase("TEST FIVE")
uppercase("")"""
