#!/usr/bin/python3
"""
Contains Square class
module path: models.square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Syntax:
        Square(size, x=0, y=0, id=None)

    Description:
        Square is a class wich represents the square shape, inherits from
        the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Consitructer which initiate the Square instance with the size,
        x, y, and id, the initiate is done by the super class Rectangle
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Implementing the str method for the Square class instances
        """

        return r"[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.width)

    @property
    def size(self):
        """
        Return the self.__width for the Square class instances
        """

        return self.width

    @size.setter
    def size(self, val):
        """
        set the self.__width and self.__height to the value val
        """
        self.validate("width", val)
        self.width = val
        self.validate("height", val)
        self.height = val

    def update(self, *args, **kwargs):
        """
        Syntax:
            Rectangle.update(self, *args, **kwargs)

        Description:
            Updates the Rectangle instance attributes definded on the *args
            list starting by the `id`, `width`, `height`, `x`, and `y`, or
            by using the **kwargs
        """

        if len(args) >= 1:

            # super().__init__(args[0])
            super().update(args[0])
            for i in range(1, len(args)):
                if i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.validate("x", args[i])
                    self.x = args[i]
                elif i == 3:
                    self.validate("y", args[i])
                    self.y = args[i]
        else:

            for key, val in kwargs.items():
                if key == "id":
                    super().update(val)
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.validate(key, val)
                    self.x = val
                elif key == "y":
                    self.validate(key, val)
                    self.y = val

    def to_dictionary(self):
        """
        Syntax:
            Rectangle.to_dictionary(self)

        Description:
            Return a Dictionary contains the instance attributs
        """

        __dic = dict()
        __dic['size'] = self.size
        __dic['x'] = self.x
        __dic['y'] = self.y
        __dic['id'] = self.id
        return __dic
