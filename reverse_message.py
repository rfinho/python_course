word = ""
msg = input("Please write your message: ")
i = 0

print("======= Your Message =======")
while i < len(msg):
    if msg[i] == " ":
        print(word[::-1])
        word = ""
    else:
        word += msg[i]
    i +=1
print(word[::-1])
