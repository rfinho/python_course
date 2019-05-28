msg = input("Enter your message: ")
findChar = input("What are you looking for?: ")
i = 0
counter = 0
print("======= Your Message =======")
while i < len(msg):
    if msg[i] == findChar:
        counter += 1
    i += 1
print(counter)