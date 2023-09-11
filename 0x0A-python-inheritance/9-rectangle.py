#!/usr/bin/python3
"""
Contains the Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def __str__(self):
        """
        Implementing str() and set custom string for it
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Syntax:
            Rectangle.area(self)
        Description:
            Calculate the Rectangle area and return the result
        """

        return self.__width * self.__height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))
    print(r.area())

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
