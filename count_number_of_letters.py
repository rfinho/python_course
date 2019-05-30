alphabetLower = [0] * 26
alphabetUpper = [0] * 26
characters = []
message = input(("Please write your message: "))
i = 0

for i in range (len(message)):
    if 65 <= ord(message[i]) <= 90: 
        alphabetUpper[ord(message[i]) - 65] += 1
    elif 97 <= ord(message[i]) <= 122:
        alphabetLower[ord(message[i]) - 97] += 1
    else:
        characters.append(i)
    

x = 0
while x <= 25:
    if alphabetUpper[x] > 0:
        print(chr(x + 65), "=", alphabetUpper[x])
    if alphabetLower[x] > 0:
        print(chr(x + 97), "=", alphabetLower[x])
    x += 1
