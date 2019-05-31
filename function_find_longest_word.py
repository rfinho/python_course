def maxName(text):
    word = ""
    text += " "
    words = []
    for x in text:
        if x == " ":
            words.append(word)
            word = ""
        else:
            word += x
    print(max(words, key=len))


input_text = input("Enter your message ot find longets word: ")
maxName(input_text)
