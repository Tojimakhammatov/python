
#While

name = input("What is your name? ")
question = f"Hi, {name.title()}. How old are you? "
age = input(question)
age = int(age) # funksiya int - age ni stirdan integerga o`tkazadi.

height = input("how is your height? ")
height = float(height) # funksiya float sonni o`nlik songa beradi

# WHILE tsikli - toki 

number = 1 # son bizda 1 ga teng
while number <=5: # toki son 5 dan kichik yoki teng ekan....
    print(number, end=' ') # sonni konsolga chiqaramiz
    number = number + 1 # songa 1 ni qo`shamiz
    # number + = 1 bu ham number = number +1 bilan bir xil
print("Game over")



# while and input

print("A program that calculates the square of an input number.")

question = "Enter any number "
question += "(Type 'exit' to end the program!): "
value = ' ' 
while value != 'exit':
    value = input(question)
    if value != 'exit':
        print(float(value)**2)
print("Program is over")



print("A program that calculates the square of an input number.")

question = "Enter any number "
question += "(Type 'exit' to end the program!): "

sign = True
while sign :
    value = input(question)
    if value == 'exit':
        sign = False
    else:
        print(float(value)**2)
print("Program is end !")



# Break 

print("A program that calculates the square of an input number.")

question = "Enter any number "
question += "(Type 'exit' to end the program!): "

while True : # abadiy tsikl
    value = input(question)
    if value == 'exit':
        break # tsiklni to`xtatish
    else:
        print(float(value)**2)
print("Program is end !")



# break for

numbers = list(range(1, 11))
for number in numbers:
    if number == 5:
        break
    print(f"{number} square is {number**2}")



numbers = list(range(1, 11))
for number in numbers:
    if number == 5:
        continue
    print(f"{number} square is {number**2}")



# # continue  While

number = 0
while number < 10 :
    number += 1
    if number%2 != 0: # sonni qoldig`i bo`lmasa. 2 ga bo`linganda
        continue
    else:
        print(number)



number = 0
while number < 10 :
   # number += 1  ushbu qator tashlab ketilsa abadiy tsiklga o`tib qolamiz
    if number%2 != 0: # sonni qoldig`i bo`lmasa. 2 ga bo`linganda
        continue
    else:
        print(number)



# quyida abadiy tsiklga misollardan biri.
number = 1 # agar son 1 ga teng bo`lsa
while number > 0: # 0 dan katta bo`lsa hisoblashda davom etilsin
    number += 1
    if number%2 != 0: 
        continue
    else:
        print(number)
        
   

# HOMEWORK

books = ("Enter your favourite book ")
books += "(Type 'exit' to end the program!): "
while True:
    book = input(books)
    if book == 'stop' :
        break
    else :
        print(book)
print(f"Thank you !")



question = ("Enter your age : ")

while True:
    age = (input(question))
    if age == 'exit' or age == 'quit':
        break
    value = int(age)


    if value <7:
        print("Ticket price 2000 sum ")
    elif value <18:
        print("Ticket price 3000 sum ")
    elif value <65:
        print("Ticket price 10000 sum ")
    else:
        print("Ticket free ")
print("Program end !")

