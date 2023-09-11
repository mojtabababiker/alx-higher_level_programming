#!/usr/bin/python3
"""
Contains the MyList class which is a subclass of List()
"""


class MyList(list):
    """
    Syntax:
        MyList()

    Description:
        MyList is a Class which inherit from the built in class List
        which provides a method of sorted printing for
        its elements.

    Methods:
        MyList.print_sorted(self)
    """

    def print_sorted(self):
        """
        Syntax:
           MyList.print_sorted(self)

        Descrtiption:
            print list elements in ascending order
        """

        sorted_list = list(self)
        sorted_list.sort()
        print(sorted_list)
