#!/usr/bin/python3
"""
Contains the improved version of the BaseGeometry class
"""


class BaseGeometry:
    """
    Syntax:
        BaseGeometry()

    Descriptions:
        An improved version of the BaseGeometry with the method
        area(self) definded
    """

    def area(self):
        """
        Syntax:
            BaseGeometry.area(self)

        Descriptions:
            Calculate the area of the self and return its value
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Syntax:
            BaseGeometry.integer_validator(self, name, value)

        Description:
            Validate the value variable if its an ineger and greater than 0
            or not
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
