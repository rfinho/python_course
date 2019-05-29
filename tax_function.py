def tax(salary):
    if salary > 1500:
        tax = salary * 20 / 100
    else:
        tax = salary * 15 / 100
    return tax


input_salary = int(input("Enter your salary: "))
print("Your tax is:", int(tax(input_salary)))
print("Your net salary is:", int(input_salary - tax(input_salary)))