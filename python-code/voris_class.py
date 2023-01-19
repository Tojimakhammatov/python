class Person:
    """person`s info"""
    
    def __init__(self, name, surname, passport, born):
        """shaxs xususiyatlari"""
        self.name = name
        self.surname = surname
        self.passport = passport
        self.born = born
    
    def get_info(self):
        """Shaxs haqida ma`lumot"""
        info = f"{self.name} {self.surname}. "
        info += f"Passport : {self.passport}, {self.born}. "
        return info

    def get_age(self, year):
        """Shaxsning yoshini beruvchi method"""
        return year - self.born

class Student(Person):
    """Class of Student"""
    def __init__(self, name, surname, passport, born, IDnumber, adress):
        """Student xususiyatlari"""
        super().__init__(name, surname, passport, born)
        self.IDnumber = IDnumber
        self.level = 1
        self.adress = adress

    def get_ID(self):
        return self.IDnumber
    
    def get_level(self):
        return self.level

    def get_info(self): #info about Student 
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_level()} - level. ID number : {self.IDnumber} "
        return info

class Adress:
    def __init__(self, homenumber, street, district, region):
        self.homenumber = homenumber
        self.street = street
        self.district = district
        self.region = region

    def get_adress(self):
        adress = f"{self.region}-region, {self.district}-district, "
        adress += f"{self.street}-street, {self.homenumber}-home"
        return adress