msg = input("Enter your message: ")
what = input("What are you looking for?: ")
msg += " "
word = ""
i = 0
counter = 0
print("======= Your Message =======")
while i < len(msg):
    if msg[i] == " ":
        if word == what:
            counter += 1 
        word = ""
    else:
        word += msg[i]
    i += 1
print(counter)
