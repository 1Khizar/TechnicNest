counter = 0  # Global variable

def change_counter():
    global counter
    counter += 1

# Example usage
change_counter()
print(counter)  # Output: 1

change_counter()
print(counter)  # Output: 2
