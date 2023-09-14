#!/usr/bin/python3
"""
base.py modules contains the class Base, which is the base class
for most of the classes in this projects
"""



class Base:
    """
    Syntax:
         Base(id=None)

    Description:
         This Class works as a container for all the comming classes

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Description:
            Conistructeor method which initiate the Base clase instence
            with the id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

