#!/usr/bin/python3
def remove_char_at(s, n):
    """
    remove_char_at - copy the string str1 to new str removing the index n value
    s: the source string to be copied
    n: the index that should be removed
    Retunr: new string
    pesudo code:
        set new_str = list
        set i = 0 for iterator counter
        if the s string is empty return Null
        loop through all the elemnts in s,
        copy the index i from it to the new_str
        if the i is == n then skip this index value
        inceament i by one
        return new_str
    """
    i = 0
    new_str = str()
    if len(s) == 0:
        return None
    while i < len(s):
        if i == n or i == len(s) + n:
            i += 1
            continue
        new_str += s[i]
        i += 1
    return new_str


if __name__ == "__main__":
    s1 = "Best School"
    s2 = ""
    print(remove_char_at(s1, 0))
    print(remove_char_at(s1, -1))
    print(remove_char_at(s1, 5))
    print(remove_char_at(s1, 30))
    print(remove_char_at(s2, 3))
