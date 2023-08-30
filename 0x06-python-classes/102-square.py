#!/usr/bin/python3
'''
   102-square: holds the Square class
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
        self.__size = size

    def __lt__(self, other):
        '''
        Custom implementation fot < operator
        '''
        return self.area() < other.area()

    def __gt__(self, other):
        '''
        Custom implementation fot > operator
        '''
        return self.area() > other.area()

    def __le__(self, other):
        '''
        Custom implementation fot <= operator
        '''
        return self.area() <= other.area()

    def __ge__(self, other):
        '''
        Custom implementation fot >= operator
        '''
        return self.area() >= other.area()

    def __eq__(self, other):
        '''
        Custom implementation fot == operator
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        '''
        Custom implementation fot != operator
        '''
        return self.area() != other.area()

    @property
    def size(self):
        '''
        property Decorator that get the __size atteripute
        '''
        return self.__size

    @size.setter
    def size(self, size):
        '''
        property Decorator that set the __size atteripute
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
