# Program to check if Password is correct or not using While loop.
password = int(input("Enter password here"))
while password != 123456:
    print("Incorrect Password, Please try again!")
    password = int(input("Enter password here"))
if password == 123456:
    print("Password is correct!")