#!/usr/bin/python3

"""
printing alphabits from z to a starting with lower case and
then interchange between lower and upper for the rest of the letters
 pesudo code:
        set up_flag = 0
        for i in rang 122 to 96 decreas it by 1
            if the up_flag is one then
                set chr = i - 32
                set up_flag = 0
            if the up_flag is zero then
                set chr = i
                set up_flag = 1
            print chr using the format function with the flag 'c'
"""
upper_case = 0
for i in range(122, 96, -1):
    if upper_case:
        char = i - 32
        upper_case = 0
    else:
        char = i
        upper_case = 1
    print(f"{format(char, 'c')}", end="")
