product = input("Enter product name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

amount = qty * price
vat = round((amount * 15 / 100),2)
bill = round((amount + vat),2)

print("============ Your bill ============")
print("Product: ", product)
print("Amount: ", amount)
print("VAT ", vat)
print("Bill ", bill)
print("===================================")