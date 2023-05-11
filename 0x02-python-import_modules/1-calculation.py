#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    print("{a} + {b} = {c}".format(a=a, b=b, c=calc.add(a, b)))
    print("{a} - {b} = {c}".format(a=a, b=b, c=calc.sub(a, b)))
    print("{a} * {b} = {c}".format(a=a, b=b, c=calc.mul(a, b)))
    print("{a} / {b} = {c}".format(a=a, b=b, c=calc.div(a, b)))
