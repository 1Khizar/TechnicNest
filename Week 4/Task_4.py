# Task 4
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(8))

print("Generated password:", password)
