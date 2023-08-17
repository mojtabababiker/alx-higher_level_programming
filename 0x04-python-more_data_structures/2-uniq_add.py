#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    ls = set(my_list)
    sum = 0
    for num in ls:
        sum += num
    return sum
