
# Dictionary
"""
car = {'car' : 'ferrari', 'colour' : 'red'}
print(car ['car'])
print(car ['colour'])

en_uz = {'aplle' : 'olma', 'orange' : 'mandarin', 'strawberry' : 'qulupnay', 'banana' : 'banan'}

print(en_uz ['orange'])

# for n in en_uz :
    # print(n)

fruits = {'aplle' : '5000', 'orange' : '12000', 'banana' : '22.900'}

print(fruits ['orange'])
print(f"price : {fruits ['orange']}")

student = {'name':'dua lipa', 'age':22, 'born':2000 }

print(f"{student['name'].title()}, \
born : {student ['born']}, \
age : {student ['age']}.")

# add information for dictionary
student ['faculty'] = 'singer'
student ['nationality'] = 'american'

print(student)

# change name
student ['name'] = 'Jenny'

print(student)

# empty bascet

student_1 = {}
student_1 ['name'] = 'harry'
student_1 ['level'] = 4
student_1 ['study'] = 'hagward'
student_1 ['age'] = 20

print(student_1)

print(f"Student name : {student_1 ['name'].title()}, \
age : {student_1 ['age']}, \
University : {student_1 ['study'].upper()}, \
course level : {student_1 ['level']} ")

# delete 

fruits = {'aplle' : '5000', 'orange' : '12000', 'banana' : '22.900'}

del fruits ['aplle']
print(fruits)

# write in lines

phones = {
    'Alisa' : 'iphone X',
    'jenny' : 'samsung s9',
    'John' : 'red mi 8',
    'Serik' : 'Iphone 11 pro'
}
print(phones)
print(phones ['Alisa'])


# Method GET
phone = phones.get('Jack', 'not available')
print(phone)


# Homework

manager = {'name':'bob', 'age':32, 'nationality':'american'}
chief = {'name':'phileas', 'age':41, 'nationality':'britain'}
boss = {'name':'kim chen ho', 'age':48, 'nationality':'japanese'}

print(f"Manager name : {manager ['name'].title()}, Age : {manager ['age']}, \
Manager nationality : {manager ['nationality'].title()}")

print(f"Chief name : {chief ['name'].title()}, \
Chief age : {chief ['age']}, Chief nationality : {chief ['nationality'].title()}")

print(f"Boss name : {boss ['name'].title()}, \
Boss age : {boss ['age']}, Boss nationality : {boss ['nationality'].title()}")

meals = {'Bond':'soup', 'jack':'snaks', 'lucy':'potato'}
print(f"Bond love {meals ['Bond']}, Lucy love {meals ['lucy']}, Jack love {meals ['jack']}")

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

print(python)
 

dictionary = {'line':'chiziq', 'time':'vaqt', 'list':'ro`yhat', 'tv':'televizor', 'juice':'sharbat'}
word = input("enter a word : ")

if word not in dictionary:
    print(f"Bunday so`z lug`atda mavjud emas")
else:
    print(f"Bu so`z tarjimasi : {dictionary [word]}")

"""