try:
    n1 = int(input("Enter your number: "))
    n2 = int(input("Enter your number: "))

    result = n1 / n2
    print("Result is: ", result)

except ValueError:
    print("Please enter only digits!")
except ZeroDivisionError:
    print("Can't divide numbers by 0")