def operations(type):
    if type == 1:
        def func(a, b):
            c = a+b
            print("Result of addition is:", c)
    if type == 2:
        def func(a, b):
            c = a-b
            print("Result of subtraction is:", c)
    return func


x = operations(2)
x(10, 3)
