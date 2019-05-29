ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "twenty ", "thirty ", "fourty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

number = int(input("Enter your number:"))
answer = ""
if number >= 1000 and number <= 9999:
    answer += ones[int(number/1000)] + " thousand "
    number %= 1000
if number >= 100:
    answer += ones[int(number/100)] + " hundred "
    number %= 100
if number >= 20:
    answer += tens[int(number/10) - 1] 
    number %= 10
if number > 0 and number <=19:
    answer += ones[number]
print(answer)
