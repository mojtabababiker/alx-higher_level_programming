#!/usr/bin/python3
''' Print all the names that defined in the improted module'''
if __name__ == "__main__":
    import hidden_4
    names = [name for name in hidden_4.__dir__() if not name[0] == '_']
    for name in names:
        print(name)
