bill = int(input("Enter your bill amount: "))
paid = int(input("Enter the amount you have paid: "))
change = bill - paid
print("Change: ", change)
twenties = 0
tens = 0
fives = 0
twos = 0
ones = 0
if change >= 50:
    print(("fifties"), int(change/50))
twenties = change % 50

if twenties >= 20:
    print(("twenties"), int(twenties/20))
tens = twenties % 20

if tens >= 10:
    print(("tens"), int(tens/10))
fives = tens % 10

if fives >= 5:
    print(("fives"), int(fives/5))
twos = fives % 5

if twos >= 2:
    print(("twos"), int(twos/2))
ones = twos % 2

if ones >= 1:
    print(("ones"), int(ones/1))
