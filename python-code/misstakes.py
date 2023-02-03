

age = input("enter your age : ")
try: #harakat qilish
    age = int(age)
except ValueError:
    print("Please, enter integer value..")
else:
    print(f"You are borin in {2023-age}")


# ZeroDivisionError

x, y = 5, 10
try:
    y/(x-5)
except ZeroDivisionError:
    print("It cannot be devided 0")


#IndexError

fruits = ["apple", "cherry", "banana"]
try:
    print(fruits[4])
except IndexError:
    print(f"In fruits have {len(fruits)} fruit")

#KeyError

user = {"username" : "James",
        "status" : "creator",
        "email" : "creator@mail.com",
        "phone" : "447848784"}

key = "email"
try:
    print(f"user : {user[key]}")
except KeyError:
    print("No such key exists here..")

# FileNotFoundError

filename = "data.txt" # unavailable file
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} not available")

#example

import json
files = ['student1.json','student2.json', 'student3.json', 'student4.json']
for filename in files:
    try:
        with open(filename) as f:
            student = json.load(f)
    except FileNotFoundError:
        print(f"{filename} not available") # pass dan ham foydalanish mumkin
    else:
        print(student['name'])

# double excepts

a = input("Enter integer value : ")
try:
    a = int(a)
    x= 20/a
except ValueError: #if user entered not integer value
    print("You must enter integer value")
except ZeroDivisionError: # if user entered 0 
    print("It cannot be devided to 0")
else:
    print(f"x={x}")


while True:
    age = input("enter your age : ")
    if age.isdigit(): # yozilgan matn raqamlardan iborat yoki yo`q tekshiradi
        age = int(age)
        break
    else:
        print(f"You are borin in {2023-age}")
