#!/usr/bin/python3
"""
Contains the Rectangle class
"""


class Rectangle(BaseGeometry):
    """
    Syntax:
        Rectangle(width, height)
    Description:
        A subclass of the BaseGeometry class, whci defines a rectangle
        shape with the width and height
    """

    def __init__(self, width, height):
        """
        Conistructor method, set the __width, and __height attributes
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
