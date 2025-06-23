import random
import string
import os

os.system("clear")
print("-------------------------") 
print("Random Password Generator")
print("-------------------------") 
print("1: Mixed ")
print("2: All Letters ")
print("3: Capital Letters ")
print("4: Lowercase letters ")
print("5: Numbers")
print("6: Symbols")
print("7: Exit ")
print("-------------------------") 
print()
choice = int(input("Make Your Choice: "))

if choice == 1:
    characters = string.ascii_letters + string.digits + string.punctuation
    os.system("clear")
    length = int(input("Enter Length: "))
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Password = " + password)

elif choice == 2:
    characters = string.ascii_letters
    os.system("clear")
    length = int(input("Enter Length: "))
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Password = " + password)

elif choice == 3:
    characters = string.ascii_uppercase
    os.system("clear")
    length = int(input("Enter Length: "))
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Password = " + password)

elif choice == 4:
    characters = string.ascii_lowercase
    os.system("clear")
    length = int(input("Enter Length: "))
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Password = " + password)

elif choice == 5:
    characters = string.digits
    os.system("clear")
    length = int(input("Enter Length: "))
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Password = " + password)

elif choice == 6:
    characters = string.punctuation
    os.system("clear")
    length = int(input("Enter Length: "))
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Password = " + password)

elif choice == 7:
    os.system("clear")
    print("Application is closing...")
    exit()

else:
    print("Invalid choice!")
