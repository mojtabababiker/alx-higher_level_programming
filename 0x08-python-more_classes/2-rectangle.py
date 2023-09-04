#!/usr/bin/python3
"""
Module that defines Rectangle class
"""


class Rectangle:
    """
    Rectangle: class that represent a rectangle shap with
    the width and height
    """
    def __init__(self, width=0, height=0):
        """
        Instance initializatoin function that set self.width and
        self.height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        decorated function to set self.__width attribute
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        decorated function to set self.__height attribute
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        Rectangle.area(self)
        Instance method which calculates the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Rectangle.perimeter(self)
        Instance method which calculates the perimeter of the
        recnatgle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
