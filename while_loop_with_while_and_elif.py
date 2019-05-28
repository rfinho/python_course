limit = int(input("Enter your limit "))
a = 1
print("========== Odd or Even? ==========")
while a <= limit:
    if a % 2 == 0:
        print(a, "is Even")
    else:
        print(a, "is Odd")
    a += 1
print("===================================")