msg = input("Enter your faveourite food: ")
i = 0
print("======= Favuorite food reversed =======")
while i < len(msg):
    print(msg[::-1][i])
    i += 1
print("===================================")