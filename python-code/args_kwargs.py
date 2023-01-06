
# FUNKTSIYA VA RO`YHAT

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting : ")
        baholar[ism] = int(baho)
    return baholar

students = ['ali', 'olim', 'jack', 'julie']
baholar = bahola(students[:])   # [:] bu ro`yhatni copy qilish uchun
print(baholar)
print(students)

##################### *args va **kwargs  #####################

def summa(*numbers):
    """kiritilgan sonlarni yig`indisini hisoblaydi"""
    yigindi = 0  #yig`indining dastlabki qiymati 0 ga teng 
    for number in numbers:
        yigindi += number
    return yigindi

print(summa(1,2))
print(summa(1,2,3,4,5,6,7))
print(summa(4,5,6,7,8))

def summa(*numbers):  # yuqoridagi kodni sum funksiyasidan foydalanib yozdik
    return sum(numbers)

print(summa(1,2))
print(summa(1,2,3,4,5,6,7))
print(summa(4,5,6,7,8))

def summa(x,y, *numbers): # x, y majburiy qiymat qabul qiluvchi
    return x+y+sum(numbers)
    
print(summa(1,2)) # bu yerda 1=x, 2=y
print(summa(1,2,3,4,5,6,7))  # bu yerda 1=x, 2=y, qolgani ixtiyoriy
print(summa(4,5,6,7,8))
print(summa(1,9))


#**kwargs   keywords

def auto_info(company, model, **info):
    """Auto lar haqida ma`lumot lug`at ko`rinishida qaytaruvchi funksiya"""
    info['company']= company
    info['model']= model
    return info

auto1 = auto_info("GM", "malibu", rang='qora', yil=2018)
auto2 = auto_info("kia", "K5", rang= 'qizil', yil=2019, narx=35000)

print(auto1)
print(auto2)

#homework

def multiply(*numbers):
    """son qabul qilib ko`paytmasini beruvchi kod"""
    result = 1
    for number in numbers:
           result *= number
    return result

print(multiply(1,2,3,4,5,6,7,8,9))
print(multiply(3,5,0.1,45))

def students(name, surname, **others):
    """talaba ma`lumoti"""
    others["name"] = name.title()
    others["surname"] = surname.title()
    return others

student1 = students('azizbek', 'tojimaxammatov', course=4, phone = 3240804, born = "andijan")
student2 = students('james', 'bond', born=1980, phone= 777777, died="october")

print(student1)
print(student2)
