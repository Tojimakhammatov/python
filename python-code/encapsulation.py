

from uuid import uuid4
class Auto:
    """class auto"""
    __num_auto = 0
    def __init__(self, make, model, color, year, price, km=0 ):
        """auto`s features"""
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Auto.__num_auto += 1

    @classmethod
    def get_num_auto(cls):
        return cls.__num_auto

    def get_km(self):
        return self.__km 

    def get_id(self):
        return self.__id

    def add_km(self,km):
        """add km auto`s km"""
        if km>=0:
            self.__km += km
        else:
            print("Error, you cannot change distance!")


class Student:
    __num_student = 0
    def __init__(self,name,surname,born, number=" "):
        self.name = name
        self.surname = surname
        self.born = born
        self.course = 1
        self.__ID = uuid4
        self.__number = number
        Student.__num_student += 1

    @classmethod
    def get_num_student(cls):
        return cls.__num_student

    def get_name(self):
        return self.name

    def get_lastanme(self):
        return self.surname

    def get_age(self,year):
        return year - self.born

    def introduce(self):
        return f"My name is {self.name} {self.surname}, born {self.born} "

    def add_number(self,number):
        if number >= 100000000:
            self.__number += number
        else:
            print("Error, number is not available!")

    def get_id(self):
        return self.__ID