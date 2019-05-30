def reverse(word):
    new_word = ""
    i = len(word) - 1

    while i >= 0:
        new_word += word[i]
        i -= 1
    return new_word


message = input("Enter your message: ")
message += " "
new_message = " "
word = ""

for x in message:
    if x == " ":
        new_message += (reverse(word)) + " "
        word = ""
    else:
        word += x
print(new_message)
