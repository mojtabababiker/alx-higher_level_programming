#!/usr/bin/python3
''' Print all the names that defined in the improted module'''
if __name__ == "__main__":
    import dis
    import hidden_4

    dis.dis(hidden_4, depth=0)
