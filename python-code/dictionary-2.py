
# lug`at elementlari bilan ishlar .items()

python = {
'string':'matn', \
'variable':'o`zgaruvchi', \
'upper':'barcha harflarni katta qilish uchun', \
'lower':'barcha ahrflarni kichik qilish uchun', \
'title':'birinchi harflarni katta qilish uchun', \
'if':'agar', \
'elif':'if dan keyingi, else dan oldingi qatorlarda keluvchi, agar', \
'for':'uchun', \
'else':'yoki, bo`lmasa',\
'list':'ro`yhat'
}

for key, word in python.items():
    print(f"key : {key}")
    print(f"word : {word}\n")



phones = {
    'Alisa' : 'iphone X',
    'jenny' : 'samsung s9',
    'John' : 'red mi 8',
    'Serik' : 'Iphone 11 pro'
}

for k, w in phones.items():
    print(f"{k.title()}'s phone {w}")


# KEYS method .keys()

fruits = {
'apple' : '5000',
'orange' : '12000', 
'banana' : '22.900'
}

print(fruits.keys())

print("Fruits in store : ")
for fruit in fruits.keys():
    print(fruit.title())

busket = ['orange', 'cherry', 'apple']
for fruit in fruits:
    if fruit in busket:
       print(f"{fruit.title()} {fruits[fruit]} sum")

for fruit in busket:
    if fruit not in fruits:
        print(f"Please bring your store {fruit} too!")



fruits = {
'pineapple' : 12000,
'apple' : 5000,
'orange' : 12000, 
'banana' : 22.900,
'watermelon' : 23000,
'cherry' : 32000
}

print(f"Fruits in our store : ")
for fruit in sorted(fruits, reverse=True):
    print(fruit.title())

print(fruits.values()) # faqat qiymatlar beradi .values()


phones = {
    'Alisa' : 'iphone X',
    'jenny' : 'samsung s9',
    'John' : 'red mi 8',
    'Serik' : 'Iphone 11 pro',
    'Philip' : 'iphone X',
    'Artur' : 'samsung s9',
    'Lucy' : 'red mi 8',
    'Dua Lipa' : 'Iphone 11 pro'
}

print('Users used : ')
for phone in phones.values():
    print(phone)

print('Users used : ')
for phone in set(phones.values()):  # set() - bu bir nechta o`xshash qiymatni bitta ko`rinishga keltirib chiqaradi.
    print(phone)                    # set - ma`lumot turidan biri

# SET
toys = {'ball', 'horse', 'cars', 'lamp', 'horse'}
print(type(toys))

print(toys)  # set ma`lumot turi 2 marta takrorlanuvchini bittasini yozadi 


# Homework

python = {
'string':'matn',
'variable':'o`zgaruvchi', 
'upper':'barcha harflarni katta qilish uchun', 
'lower':'barcha ahrflarni kichik qilish uchun', 
'title':'birinchi harflarni katta qilish uchun', 
'if':'agar', 
'elif':'if dan keyingi, else dan oldingi qatorlarda keluvchi, agar', 
'for':'uchun', 
'else':'yoki, bo`lmasa',
'list':'ro`yhat'
}
for keys, means in sorted(python.items()): # .items() orqali lug`atdagi barcha kalit va so`zni ko`rish mumkin
    print(f"{keys} - {means}")

countries = {
'USA':"Washington",
'argentina':'buenos-ayres',
'uzbekistan':'toshkent',
'rossiya':'moskva',
'singapur':'sydney'
}
if countries == 'usa':
    print(countries.upper())

for country, capital in countries.items():
    print(f"{country.title()} - {capital.title()}")

for country, capital in sorted(countries.items()):
    print(country.title())
    print(capital.title())


countries = {
'usa':'washington',
'argentina':'buenos-ayres',
'uzbekistan':'toshkent',
'russian':'moskva',
'singapur':'sydney'
}
name = input("Enter country : ")
if name.lower() in countries:
    print(f"Capital of {name.title()} : {countries [name].title()}")
else:
    print(f"We have no information about : {name.title()} ")


meals = {
'pilov' : 24000,
'soup' : 22000,
'snaks' : 6000,
'bread' : 4000,
'club' : 23000,
'tea' : 5000,
'coffee' : 7000,
'pasta' : 28000,
'norin'  : 27000,
'water' : 2000
}
print("Order 3 dishes : ")
meal = input("meal 1 : ")
meal2 = input("meal 2 : ")
meal3 = input("meal 3 : ")

if meal in meals:
    print(f"{meal} : {meals [meal]}")

if meal2 in meals:
    print(f"{meal2} : {meals [meal2]}")

if meal3 in meals:
    print(f"{meal3} : {meals [meal3]}")

if meal not in meals:
    print(f"{meal} : is not on the menu")
    
if meal2 not in meals:
    print(f"{meal2} : is not on the menu")

if meal3 not in meals:
    print(f"{meal3} : is not on the menu")

