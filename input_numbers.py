def ones(number):
    result = ""
    if number == 1:
        result = "one"
    if number == 2:
        result = "two"
    if number == 3:
        result = "three"
    if number == 4:
        result = "four"
    if number == 5:
        result = "five"
    if number == 6:
        result = "six"
    if number == 7:
        result = "seven"
    if number == 8:
        result = "eight"
    if number == 9:
        result = "nine"
    if number == 10:
        result = "ten"
    if number == 11:
        result = "eleven"
    if number == 12:
        result = "twelve"
    if number == 13:
        result = "thirteen"
    if number == 14:
        result = "fourteen"
    if number == 15:
        result = "fiveteen"
    if number == 16:
        result = "sixteen"
    if number == 17:
        result = "seventeen"
    if number == 18:
        result = "eighteen"
    if number == 19:
        result = "nineteen"
    return result


def tens(number):
    result = ""
    if number == 20:
        result = "twenty "
    if number == 30:
        result = "thirty "
    if number == 40:
        result = "tourty "
    if number == 50:
        result = "fifty "
    if number == 60:
        result = "sixty "
    if number == 70:
        result = "seventy "
    if number == 80:
        result = "eighty "
    if number == 90:
        result = "ninety "
    return result


def spell(number):
    answer = ""
    if number >= 1000 and number <= 9999:
        answer += ones(int(number/1000)) + " thousand "
        number %= 1000
    if number >= 100:
        answer += ones(int(number/100)) + " hundred "
        number %= 100
    if number >= 20:
        answer += tens(int(number/10)*10)
        number %= 10
    if number <= 19:
        answer += ones(number)
    return answer


number_input = int(input("Enter any number:"))
print(spell(number_input))