# Task 2: Grade Calculator
# Take marks of 3 subjects.
# Calculate total, percentage and assign grade:
# A (>=85), B (>=70), C (>=50), Fail (<50).

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
percentage = total / 3

# Assign grade
if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", round(percentage,2))
print("Grade:", grade)
