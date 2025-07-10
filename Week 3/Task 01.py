# Task 1: Simple Calculator
# Create a calculator that accepts two numbers and an operator (+, -, *, /, %, //, **).
# Perform the operation and display the result.
# Handle division by zero safely.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %, //, **): ")


if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
elif op == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Cannot divide by zero"
elif op == '//':
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Cannot divide by zero"
elif op == '**':
    result = num1 ** num2
else:
    result = "Invalid operator"

print("Result:", result)

