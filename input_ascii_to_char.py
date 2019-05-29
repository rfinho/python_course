
def ord_to_char(input):
    if ord(input) >= 65 and ord(input) <= 90:
        print("UPPER CASE")
    else:
        if ord(input) >= 97 and ord(input) <= 122:
            print("lower case")
        else:
            if ord(input) >= 48 and ord(input) <= 57:
                print("digit")
            else:
                print("any other character")


def reverse_char_case(input):
    if ord(input) >= 65 and ord(input) <= 90:
        print(chr(ord(input) + 32))
    else:
        if ord(input) >= 97 and ord(input) <= 122:
            print(chr(ord(input) - 32))


def change(message):
    char = ""
    i = 0
    while i < len(message):
        if ord(message[i]) >= 65 and ord(message[i]) <= 90:
            char += chr(ord(message[i]) + 32)
            print(char)
        else:
            if ord(message[i]) >= 97 and ord(message[i]) <= 122:
                char += chr(ord(message[i]) - 32)
                print(char)
            else: 
                if ord(message[i]) >= 48 and ord(message[i]) <= 57:
                    char += str(int(chr(ord(message[i]))) * 2)
                    print(char)
                else:
                    char += chr(ord(message[i]))
                    print(char)

        i += 1
    return char

input_char = input("Enter your characters: ")

# print("Your character is written in: ")
# ord_to_char(input_char)

# print("reversed character: ")
# reverse_char_case(input_char)

print("TEST:")
change(input_char)
