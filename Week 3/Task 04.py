#  Task 4:
# Build a login system. Ask username & password.
# If username = 'admin' and password = '1234', print Access Granted.
# Else, Access Denied.

username = input("Enter the username : ")
password = input("Enter the password : ")

if username == 'admin' and password =='1234':
    print("Access Granted.")
else:
    print("Access  Denied")