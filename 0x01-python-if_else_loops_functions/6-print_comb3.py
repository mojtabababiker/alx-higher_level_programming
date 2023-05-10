#!/usr/bin/python3
i = 0
j = 0

while (i < 10):
    if i == 8 and j == 9:
        print(f"{i}{j}")
        break
    if i != j:
        print(f"{i}{j}, ", end='')
    j += 1
    if j != 10:
        continue
    j = i + 2
    i += 1
