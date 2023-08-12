#!/usr/bin/python3
def multiple_returns(sentence):
    '''
    Check the length of sentence and its first charcter

    Args:
        sentence - the sentence to check its length and first charcter
    Return:
        A tuple of the sentence length and the first charcter, or None
        for the first charcter and 0 for the lenght in fialure
    '''
    lenght = len(sentence)
    if lenght == 0:
        return (0, None)

    return (lenght, sentence[0])
