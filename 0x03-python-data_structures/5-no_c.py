#!/usr/bin/python3
def no_c(my_string):
    '''
        Remove all the characters `c` and `C`from my_srting

        Args:
            my_srting - remove the characters from it

        Retunr:
            the new srting
    '''
    return ("".join([c for c in my_string if c != 'c' and c != 'C']))


if __name__ == "__main__":
    no_c("OCCCCCCCCCCCCCCCCCCCCccccccc_cccccccccccccccccO")
