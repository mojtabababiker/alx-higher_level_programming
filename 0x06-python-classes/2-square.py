#!/usr/bin/python3
'''
   2-square module Holds the Square class decliaration
'''


class Square:
    '''
    Square(size=0): a square class with a privet attribute size
    and setter method
    '''

    def __init__(self, size=0):
        '''
        constructer method
        '''
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size
