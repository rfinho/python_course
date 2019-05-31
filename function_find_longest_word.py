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


maxName("hello my friend")
