numbers = [5, 23, 8, 2, 11, 77]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


highest = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > highest:
        highest = numbers[i]
    i += 1
print("Highest number is:", highest)
