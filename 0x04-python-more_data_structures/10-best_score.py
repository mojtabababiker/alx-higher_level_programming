#!/usr/bin/python3
def best_score(a_dictionary: dict) -> str:
    '''
    get the key withe biggest integer value

    Args:
        a_dictionary - the dictionary to search at

    Return:
        the key with the beggist value
    '''
    max_key = None
    if a_dictionary is None:
        return max_key

    for key, value in a_dictionary.items():
        if max_key is None or a_dictionary[max_key] < value:
            max_key = key

    return (max_key)
