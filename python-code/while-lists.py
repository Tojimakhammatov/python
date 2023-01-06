

# PYTHON 

# while and lists

print("Enter name your friends")

friends = [] # bu ro`yhat
n=1

while True:
    question = f"Enter {n} name your friend : "
    name = input(question)
    friends.append(name)
    remember = input("Do you want add any? (Yes/No) ")
    n += 1
    if remember.lower() != 'yes' :
        break
    
print("Your friends list : ")
for name in friends:
    print(name.title())
    


print("Save your friends age.")
friends = {}
hint = True
while hint :
    name = input("Enter your friend name : ")
    age = input("Enter your friend age : ")
    friends[name] = int(age)
    
    question = input("Do you want add any value ?  (Yes/No) ")
    if question.lower() == "no":
        hint = False

for name, age in friends.items():
    print(f"{name.title()} : {age}")



cars = ['audi', 'jentra', 'spark', 'audi', 'toyota', 'nexia', 'audi']
car = 'audi'

while car in cars:
    cars.remove(car)

print(cars)



students = ['Dua', 'Lipa', "jenny", 'james']
graded_students ={}

while students:
    student = students.pop()
    score = input(f"Enter {student.title()}`s score: ")
    print(f"{student.title()} was scored.")
    graded_students[student] = int(score)

print(graded_students)



print("Mahsulotlar ro`yhatini ko`rsatuvchi dastur")
products = []
n = 1

while True :
    product = input(f"Enter your {n} product : ")
    products.append(product)
    print(f"{product} was entered.")
    remember = input("Do you want any? : (Yes/No) ")
    n += 1
     
    if remember.lower() == 'no':
        break

print(f"Your box : {products}")

    
print("e-bozor uchun shakllangan mahsulot va narxlar ro`yhati.")
products = {}
n = 1
while True:
    product = input(f"Select {n} - product : ")
    price = input("Product`s price : ")
    products[product] = float(price)
    n += 1
    
    question = input("Do you want add any value ?  (Yes/No) ")
    if question.lower() == 'no':
        break
    
for product, price in products.items():
    print(f"{product.title()} : {price}")



buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")

