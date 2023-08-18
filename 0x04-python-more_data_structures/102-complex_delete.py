#!/usr/bin/python3
def complex_delete(a_dictionary: dict, value: any) -> dict:
    '''
    Delete keys in a dictionary with a specific value

    Args:
        a_dictionary - dictionary
        value - the value of the requiered keys

    Retrun:
        A new dictionary without all the keys with the value value
    '''
    new_dict = dict()
    for key, val in a_dictionary.items():
        if val != value:
            new_dict.setdefault(key, val)
    return (new_dict)
