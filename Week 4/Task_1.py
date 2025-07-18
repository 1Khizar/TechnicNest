value = input("Enter any value: ")
print("Data type of your input:", type(value))

# Ask for a Python command to run
code = input("Enter a Python command to run (e.g., print('Hello')): ")
exec(code)
