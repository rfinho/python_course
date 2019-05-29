def word_count(message):
    word = 1
    i = 0

    while i < len(message):
        if message[i] == " ":
            word += 1
        i += 1
    return word


input_message = input("Enter your message: ")
print("Word count in your message:", word_count(input_message))
