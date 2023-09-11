#!/usr/bin/python3
"""
Contains the Square class which is a subclass of the Rectangle class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Syntax:
        Square(size)
    Description:
        A subclass of the Rectangle class which represents a Square
        shape with the size `size`
    """

    def __init__(self, size):
        """
        Consitructer method, sset the self.__size attribute
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
    print(dir(s))
