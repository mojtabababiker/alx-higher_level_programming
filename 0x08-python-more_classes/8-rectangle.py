#!/usr/bin/python3
"""
Module that defines Rectangle class
"""


class Rectangle:
    """
    Rectangle: class that represent a rectangle shap with
    the width and height
    """
    number_of_instances = 0
    print_symbol = '#'

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
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
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
    def height(self, height):
        """
        decorated function to set self.__height attribute
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """
        Implementing custom __str__ method for the Rectangle object
        """
        __rectanglestr = ""
        if self.__width == 0:
            return ""

        for i in range(self.__height):
            for _ in range(self.__width):
                __rectanglestr += str(self.print_symbol)
            if i != self.__height - 1:
                __rectanglestr += '\n'
        return __rectanglestr

    def __repr__(self):
        """
        Implementing custom __repr__ method for the Rectangle object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Implementing custom delettion __del__ method for the
        Rectangle object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A static method that return the bigger rectangle depending on
        it's area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
