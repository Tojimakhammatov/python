


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
        self.__id = uuid4
        Auto.__num_auto += 1

    def __str__(self):
        """ __str__ it will be give more understable version"""
        return f"Auto: {self.make} {self.model}"

    def __repr__(self): 
        """ __repr__ = __str__ , usually __repr__ is recommended """
        return f"Auto: {self.make} {self.model}"

    def __eq__(self,y):
        """ __eq__ tengmi?"""
        return self.price == y.price

    def __lt__(self,y):
        return self.price < y.price

    def __le__(self,y):
        return self.price <= y.price

auto1 = Auto("Ford", "Mustang", "red", 2021, 60000)
auto2 = Auto("GM", "Tahoe", "black", 2022, 70000)


class Cardealer:
    """ class Car dealership """
    def __init__(self, name):
        self.name = name 
        self.cars = []

    def __repr__(self):
        return f"{self.name} car dealership"

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        """ with this, we can see all items """
        return self.cars[index]

    def __setitem__(self, index,value):
        self.cars[index] = value
    
    def add_auto(self, *value):
        for auto in value:
            if isinstance(auto, Auto):
                self.cars.append(auto)
            else:
                print("Enter the car... ")

dealer1 = Cardealer("MaxAuto")

auto1 = Cardealer("Ford", "Mustang", "red", 2021, 60000)
auto2 = Cardealer("GM", "Tahoe", "black", 2022, 70000)
Cardealer.add_auto(auto1, auto2)