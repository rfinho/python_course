number = int(input("Enter your number: "))
limit = int(input("Enter your limit "))
a = 1
print("====== Multiplication table ======")
while a <= limit:
    print(number, "x", a, "=", (number * a) )
    a += 1
print("===================================")