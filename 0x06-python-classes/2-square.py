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
        conistrocter method
        '''
        self.__set_size(size)

    def __set_size(self, size):
        '''
        Square.set_size(self, size):

        Args:
            self: placeholder for the object
            size: the square size
        '''
        try:
            if size < 0:
                self.__size = 0
                raise ValueError("size must be >= 0")
        except TypeError:
            self.__size = 0
            raise TypeError("size must be an integer")
        self.__size = size
