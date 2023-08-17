#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    new_set = set()

    if set_1 is None and set_2 is None:
        return (None)
    if set_1 is None:
        return (set([lem for lem in set_2]))
    if set_2 is None:
        return (set([lem for lem in set_1]))

    for elm in set_1:
        if not (elm in set_2):
            new_set.add(elm)

    for elm in set_2:
        if not (elm in set_1):
            new_set.add(elm)

    return (new_set)
