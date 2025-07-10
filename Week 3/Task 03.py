# Task 3
# Ask user for monthly income and expenses.
# Calculate savings and classify:
# >10000 = Saving Well, 5000–9999 = Average, <5000 = Try to Save.

income = float(input("Enter your income : "))
expenses = float(input("Enter your expenses : "))

savings = income - expenses

if expenses > 10000:
    print("Saving well")
elif expenses >= 5000 and expenses <=9999:
    print("Average")
else:
    print("Try to save.")

