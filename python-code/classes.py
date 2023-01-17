
class Student:
    def __init__(self,name,surname,born):
        self.name = name
        self.surname = surname
        self.born = born
        self.course = 1

    def get_name(self):
        return self.name

    def get_lastanme(self):
        return self.surname

    def get_age(self,year):
        return year - self.born

    def introduce(self):
        return f"My name is {self.name} {self.surname}, born {self.born} "

Student1 = Student('Dua', 'Lipa', 1998)
Student2 = Student('Jessica', 'Belluci', 1980)
Student3 = Student('James', 'Bond', 1970)

Student1.get_name()
Student1.get_age(2023)
Student1.introduce()
 
class Sciense():
    def __init__(self, name):
        self.name = name
        self.student_number = 0
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.student_number +=1
    def get_students(self):
        return [Student.get_fullname() for student in self.students]

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__')]

math = Sciense("Math")

math.add_student(Student1)
math.add_student(Student2)
math.add_student(Student3)
