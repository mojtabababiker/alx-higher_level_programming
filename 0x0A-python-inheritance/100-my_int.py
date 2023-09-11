#!/sur/bin/python3
"""
Contains the MyInt class
"""


class MyInt(int):
    """
    A subclass of the int python builtin class, which overload the
    __eq__ and __nq__ class methods
    """

    def __init__(self, value):
        """
        Conistructor methood
        """

        self.__value = value

    def __ne__(self, other):
        """
        A class methos for the `==` logical operation
        """
        if type(other) not in [MyInt, int, float]:
            return False
        if self.__value > other or self.__value < other:
            return False
        return True

    def __eq__(self, other):
        """
        A class methos for the `==` logical operation
        """
        return not (self.__ne__(other))


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print("my_i == 3 : {}".format(my_i == 3))
    print("my_i != 3 : {}".format(my_i != 3))
    print("my_i == 'a' : {}".format(my_i == 'a'))
    print("my_i != 'a' : {}".format(my_i != 'a'))
