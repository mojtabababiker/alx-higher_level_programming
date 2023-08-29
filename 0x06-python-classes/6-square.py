#!/usr/bin/python3
"""
    6-square-module
    contains the last version of Square class

"""


class Square:
    '''
    Sauare(size=0, position=(0, 0))
    Square: square class which creat a square print it and shape it
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        called on opject creation
        the initiate method used to set the object size and position

        Args:
            size=0: int
            position=(0, 0): tuple
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        Decoritor for get self.size value
        '''
        return self.__size

    @size.setter
    def size(self, size):
        '''
        Decoritor for set self.size value

        Args:
            size: int the value to be set
        '''
        try:
            if size < 0:
                self.__size = 0
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            self.__size = 0
            raise TypeError("size must be an integer")

    @property
    def position(self):
        '''
        Decoritor for get self.position value
        '''
        return self.__position

    @position.setter
    def position(self, position):
        '''
        Decoritor for set self.position value

        Args:
            position: tuple  the value to be set
        '''
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or position < (0, 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''
        self.area()
        Calculate and return the area of a square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        my_print()
        print # samples thats represent the square
        '''
        __spaces = self.__position[0]
        __lines = self.__position[1]
        if self.__size == 0:
            if __lines != 0:
                print("\n" * __lines, end="")
        else:
            for i in range(__lines):
                print()
            for i in range(self.__size):
                print(' ' * __spaces, end='')
                for j in range(self.__size):
                    print("#", end='')
                print()


if __name__ == "__main__":

    my_square_1 = Square(-1)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("-size 0, pos 3-")

    my_square_3 = Square(0, (0, 3))
    my_square_3.my_print()

    print("-size 0, pos 0-")

    my_square_3 = Square(0, (0, 2))
    my_square_3.my_print()

    print("-tulep more 3-")

    my_square_3 = Square(0, [3, 3, 4])
    my_square_3.my_print()

    print("--")
