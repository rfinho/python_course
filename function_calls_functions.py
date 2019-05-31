def operation(func, a, b):
    func(a, b)


def subtraction(a, b):
    c = a - b
    print("Result of subtraction is:", c)


def addition(a, b):
    c = a + b
    print("Result of addition is:", c)


operation(addition, 30, 10)
