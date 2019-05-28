msg = input("Enter your message: ")
word = ""
inverse_message = len(msg) - 1
print("======= Your Message =======")
while inverse_message >= 0:
    if msg[inverse_message] == " ":
        print(word[::-1])
        word = ""
    else:
        word += msg[inverse_message]
    inverse_message -= 1
print(word[::-1])