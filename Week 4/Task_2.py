expression = input("Enter a Python expression (like 2 + 3 * 4): ")
print("Result of the expression is:")
exec(f"print({expression})")
