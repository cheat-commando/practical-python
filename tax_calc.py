subtotal = int(input('How much is the item worth? '))
tax = float(input("What is the sales tax where you live (express as a percent without typing the %)? ")) / 100 + 1

total = round(subtotal * tax,2)
print("Your total is: $",total, sep='')
