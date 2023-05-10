#!/usr/bin/python3
i = 0
j = 0

while (i < 10):

    if i == 9 and j == 9:
        print(f"{i}{j}")
        break
    else:
        print(f"{i}{j}, ", end='')

    j += 1
    if j != 10:
        continue
    j = 0
    i += 1
