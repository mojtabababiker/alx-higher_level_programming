#!/usr/bin/python3
def weight_average(my_list=[]) -> float:
    '''
    Return the weight average of all integers tuple (<score>, <wieght>)

    Args:
        my_list - list of tuples [(<score>, <wieght>), ...]

    Return:
        The average of all integers wieght
    '''
    score_sum = 0
    wieght_sum = 0
    if len(my_list) == 0:
        return (0)
    for t in my_list:
        score_sum += t[0] * t[1]
        wieght_sum += t[1]
    return (score_sum/wieght_sum)
