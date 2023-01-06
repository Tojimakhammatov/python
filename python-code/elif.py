

from errno import EAFNOSUPPORT
from operator import truediv


age = int(input("How old are you? " ))
if age < 4 :
    cost = 0
elif age <=12:
    cost = 4000
elif age <= 18:
    cost = 8000
else:
    cost = 10000
    
print(f"Ticket price {cost}, sum.")


day = input("What day is today? \n >> ")
if day.lower()=='saturday' or day.lower()== 'sunday':
   print('Today is a day off')
else:
    print('Today is work day')
    
day = input('What day is today? ')
temperature = float(input('what is the temperature? '))

if day.lower()== 'sunday' and temperature <= 30 :
    print('Let`s go to swimming!')
elif day.lower()== 'sunday' and temperature > 30 :
    print('We rest at home !')
else:
    print('Go to your work !!!')

meal = 15000
tea = True
salad = False
if tea and salad:
    price = meal + 10000
if tea or salad:
    price = meal + 5000

print(f"Total price : {price} ")

meal = 12000
bread = True
coffee = True
milk = False
assorti = False
if bread :
    print('Bought a bread')
    cost = meal + 3000
if coffee :
    print('Bought coffee')
    cost = cost + 5000
if milk :
    print('Bought milk')
    cost = cost + 2000
if assorti :
    print('assorti bougth')
    cost = cost + 15000
print(f"Total price : {cost}")
    

# in 
menu = ['pilov', 'meat', 'snaks', 'fries', 'coca cola']
meal = input('What do you want? \n >> ')
if meal.lower() in menu :
    print('entered')
else:
    print('We didn`t have this meal')

# not in

menu = ['pilov', 'meat', 'snaks', 'fries', 'coca cola']
meal = input('What do you want? \n >> ')
if meal.lower() not in menu :
    print('We didn`t have this meal')
else:
    print('entered')   
 
 
   
menu = ['pilov', 'meat', 'snaks', 'fries', 'coca cola']
order = ['meat', 'coca cola', 'snaks', 'potato', 'chips']


if order:
    for meal in order:
        if meal in menu:
            print(f"in menu have {meal}")
        else:
            print(f"Sorry, in menu did not have a {meal}")
       

# homework


number = float(input('Please, enter even number \n >> '))
if number %2!=0:
    print('This number is not even number ! ')
else:
    print('Thank you')


age = int(input('Please, enter your age : '))
if age<4 or age>60:
    cost = 0
elif age<18:
    cost = 10000
elif age>18:
    cost = 20000

print(f"For you ticket price : {cost} ")


from itertools import product


print('please enter two numbers')
number = float(input('First number : '))
number2 = float(input('Second number : '))
if number == number2 :
    print(f"{number} = {number2}")
elif number > number2 :
    print(f"{number}>{number2}")
else:
    print(f"{number}<{number2}")


products = ['grape', 'melon', 'apple', 'cherry', 'banana',
            'orange', 'strawberry', 'pineapple', 'snaks']
product = []
for n in range (5):
    product.append(input(f"Add {n+1} product : "))
    
if product:
    for prod in product:
        if prod in products:
            print(f"{prod} is available in our store.")
        elif prod not in products :
            print(f"{prod} is not available our store.")
else:
    print("Your basket is empty.")


products = ['grape', 'melon', 'apple', 'cherry', 'banana',
            'orange', 'strawberry', 'pineapple', 'snaks']

product = [] 
for n in range (5):
    product.append(input(f"Add {n+1} product : "))

available = []
not_available = []
for prod in product:
    if prod in products:
        available.append(prod)
    else:
        not_available.append(prod)

if not_available:
    print("Our store not : ")
    for prod in not_available:
        print(prod)
else:
    print("Our store has all the products you asked for")


users = ['Anvar', 'Maxmud', 'Botir', 'Sardor', 'Lipa']

login = input('Please, enter your log in : ')

if login.title() in users:
    print(f"this login was used")
else:
    print(f"Welcome {login.title()}")



number = int(input("Please, enter your number: "))

for n in range(2,11):
    if not (number%n):
        print(f"{number} devided {n}")


