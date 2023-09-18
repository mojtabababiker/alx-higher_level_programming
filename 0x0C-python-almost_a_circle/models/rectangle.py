#!/usr/bin/python3
"""
Containse the Rectangle class implementations
"""


from models.base import Base


class Rectangle(Base):
    """
    Syntax:
        Rectangle(width, height, x=0, y=0, id=None)

    Descriptioin:
        A class that represents the basics of the rectangle shape
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Conistructor method, which initiate the Rectangle instnace with
        width, height, x, y, and initiate the super class with the
        instance itself and id
        """
        self.validate("width", width)
        self.__width = width
        self.validate("height", height)
        self.__height = height
        self.validate("x", x)
        self.__x = x
        self.validate("y", y)
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """
        implementing of the str method
        """
        return r"[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x, self.__y,
                                                        self.__width,
                                                        self.__height)

    @property
    def width(self):
        """
        A property decorator of width getter function, wich returns
        the value of self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A decorator of width setter function, wich set the self.__width
        with the value `value`
        """
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """
        A property decorator of height getter function, wich returns
        the value of self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A decorator of height setter function, wich set the self.__height
        with the value `value`
        """
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """
        A property decorator of x getter function, wich returns
        the value of self.__x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        A decorator of x setter function, wich set the self.__x
        with the value `value`
        """
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """
        A property decorator of y getter function, wich returns
        the value of self.__y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        A decorator of y setter function, wich set the self.__y
        with the value `value`
        """
        self.validate("y", value)
        self.__y = value

    def validate(self, attrName, attrvalue):
        """
        private method of validation the class attributes
        """
        if type(attrvalue) not in [int]:
            raise TypeError("{} must be an integer".format(attrName))
        if attrName in ["width", "height"]:
            if attrvalue <= 0:
                raise ValueError("{} must be > 0".format(attrName))
        elif attrName in ["x",  "y"]:
            if attrvalue < 0:
                raise ValueError("{} must be >= 0".format(attrName))

    def area(self):
        """
        Syntax:
            Rectangle.area(self)

        Description:
            Calculate the area of the Rectangle instance and return its value
        """

        return self.__width * self.__height

    def display(self):
        """
        Syntax:
            Rectangle.display(self)

        Description:
            Print the shape of rectangle using the `#` symbol
        """
        __shape = ""

        for _ in range(self.__y):
            print()
            __shape += "\n"
        for _ in range(self.__height):
            print(" " * self.__x, end='')
            __shape += " " * self.__x
            for _ in range(self.__width):
                print("#", end='')
                __shape += "#"
            print()
            __shape += "\n"
        return __shape

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
            super().__init__(args[0])
            for i in range(1, len(args)):
                if i == 1:
                    self.validate("width", args[i])
                    self.__width = args[i]
                elif i == 2:
                    self.validate("height", args[i])
                    self.__height = args[i]
                elif i == 3:
                    self.validate("x", args[i])
                    self.__x = args[i]
                elif i == 4:
                    self.validate("y", args[i])
                    self.__y = args[i]
        else:
            for key, val in kwargs.items():
                if key == "id":
                    super().__init__(val)
                elif key == "width":
                    self.validate(key, val)
                    self.__width = val
                elif key == "height":
                    self.validate(key, val)
                    self.__height = val
                elif key == "x":
                    self.validate(key, val)
                    self.__x = val
                elif key == "y":
                    self.validate(key, val)
                    self.__y = val

    def to_dictionary(self):
        """
        Syntax:
            Rectangle.to_dictionary(self)

        Description:
            Return a Dictionary contains the instance attributs
        """

        __dic = dict()
        __dic['width'] = self.width
        __dic['height'] = self.height
        __dic['x'] = self.x
        __dic['y'] = self.y
        __dic['id'] = self.id
        return __dic
