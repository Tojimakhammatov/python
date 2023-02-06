

class Auto:
    """class auto"""
    def __init__(self, make, model, year, km=0, price = None):
        """auto`s features"""
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km

    def set_price(self, price):
        self.price = price
    
    def add_km(self, km):
        if km>0:
            self.__km += km
        else :
            raise ValueError ("please, enter "+" value..")
        
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f"{self.year}-year, {self.__km} km"
        if self.price:
            info+= f"Price : {self.price}"
        return info
    
    def get_km(self):
        return self.__km
