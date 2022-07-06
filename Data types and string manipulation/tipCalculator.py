import math

print("Welcome to de tip calculator!")
price = float(input("What was the total bill?\n"))
people = int(input("How many people to split the bill?\n"))
porcent = int(input("What percentage tip would you like to give?\n"))


price = porcent / 100 * price + price
tip = price / people
print(f"Each Person shoud pay {tip:.2f}")
