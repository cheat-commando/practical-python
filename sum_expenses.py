total = 0

num_expenses = int(input("How many expenses do you have?\nEnter a positive number.\n"))
expenses = []
for i in range(1, num_expenses + 1, 1):
    expenses.append(float(input("Enter the value of expense number " + str(i) + ': ')))

print("Your expenses sum to: $", round(sum(expenses),2), sep = '')