

# #not recommended
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close() 


# #recommended
# with open('pi.txt') as file:
#     pi = file.read()

# print(pi)
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = pi.float(pi)
# print(pi)


# filename = 'data/students.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     students = file.readlines()

# print(students)

# students = [student.rstrip() for student in students]
# print(students)


# # words will write line
# filename = 'new_file.txt'
# name = 'Dua Lipa'
# born = 1998
# with open(filename, 'w') as file: # 'w' - write
#     file.write(name)
#     file.write(str(born))

# filename = 'new_file.txt'
# name = 'Dua Lipa'
# born = 1998
# with open(filename, 'w') as file:
#     file.write(name+ '\n')
#     file.write(str(born)+ '\n')

# filename = 'new_file.txt'

# with open(filename, 'a') as file: #'a' - append
#     file.write('James Bond\n')
#     file.write('2000')


# #for dictionary or numbers etc.
# import pickle

# student1 = {'name':'Dua', 'surname':'Lipa', 'born':1998, 'course': 4}
# student2 = {'name':'Bond', 'surname':'James', 'born':1988, 'course': 1}

# with open('info'.pkl, 'wb') as file: #'wb' - write Binary
#     pickle.dump(student1,file)
#     pickle.dump(student2,file)

# print(student1)
# print(student2)

# H/W


with open("C:\Users\User\Documents\GitHub\python\python\python-code\pi.txt") as file:
    pi = file.read()
pi = pi.rstrip()  # qator ohiridagi bo'shliqlarni olib tashlash
pi = pi.replace("\n", "")  # qator tashlash belgisini almashtirish
pi = pi.replace(" ", "")

# have my birthday in PI?
bdate = "23042000"
print(bdate in pi)


