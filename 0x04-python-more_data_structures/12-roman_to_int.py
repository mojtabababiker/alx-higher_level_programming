#!/usr/bin/python3
def roman_to_int(r_string: str) -> int:
    '''
    convert a string of roman numerals into the equivalent integer
    value

    Args:
        r_string - a stirng consists of roman numerals, eg:
        "LXXXVII"

    Return:
        the equivalent integer value for the roman numerals, eg:
        87
    '''
    r_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    int_value = 0
    i = 0

    if r_string is None:
        return 0

    while i < len(r_string):
        if i < len(r_string) - 1:
            if r_values[r_string[i]] >= r_values[r_string[i + 1]]:
                int_value += (r_values[r_string[i + 1]]
                              + r_values[r_string[i]])
                i += 2
                continue
            else:
                int_value += (r_values[r_string[i + 1]]
                              - r_values[r_string[i]])
                i += 2
                continue
        else:
            int_value += r_values[r_string[i]]
            i += 1

    return (int_value)
