#!/usr/bin/python3
"""
Locked class module
"""


class LockedClass:
    """
    LockedClass that not allowing any atteribute assigning
    except the sel.name
    """
    def __setattr__(self, attr, value):
        if attr == "first_name":
            self.__dict__[attr] = value
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attr))


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    print(lc.__dict__)
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
