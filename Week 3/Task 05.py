#  Task 5:
# Ask user for attendance (%) and final marks.
# If attendance ≥ 75 and marks ≥ 50 → Promote
# Else → Not promoted.

attendance = float(input("Enter your attendance(%) : "))
marks = float(input("Enter your marks : "))

if attendance >= 75 and marks >= 50:
    print("Promote")
else:
    print("Not promoteed.")

