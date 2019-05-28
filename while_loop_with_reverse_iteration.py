msg = input("Enter your faveourite food: ")
i = 0
print("======= Favuorite food reversed =======")
while i < len(msg):
    print(msg[i][::-1])
    i += 1
print("===================================")