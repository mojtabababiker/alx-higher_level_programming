#!/usr/bin/python3
'''
   3-square: holds the Square class
'''


class Square:
    '''
       Square(size=0)

       Args:
           size: int defaulat 0 the size of the square
    '''

    def __init__(self, size=0):
        '''
           the initiate function/constructor method
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
            self.__size = size
        except TypeError:
            self.__size = 0
            raise TypeError("size must be an integer")

    def area(self):
        '''
        Square.area(self)

        Description:
              Use to calculate the sqauare are and return the result
        '''
        return self.__size ** 2
