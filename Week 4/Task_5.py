# Task 5
from datetime import datetime

birth_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_input, "%Y-%m-%d")
today = datetime.now()

age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
days_lived = (today - birth_date).days

print("You are", age_years, "years old.")
print("You have lived for", days_lived, "days.")
