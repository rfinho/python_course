word = 0
msg = input("Enter your message: ")
i = 0
print("========= How many words? =========")
while i < len(msg):
    if msg[i] == " ":
        word += 1
    i += 1
print("There are", (word + 1), "words")
print("===================================")