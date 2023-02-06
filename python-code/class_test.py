
import unittest
from class_car import Auto
"""code for check class car"""

class AutoTest(unittest.TestCase):
    def setUp(self):
        make = "Ford"
        model = "Mustang"
        year = 2022
        self.price = 55000
        self.km = 4000
        self.auto1 = Auto(make,model,year)
        self.auto2 = Auto(make,model,year,price=self.price)

    def test_create(self):
        #Value mavjudligini - assertIsNotNone
        self.assertIsNotNone(self.auto1.make)
        self.assertIsNotNone(self.auto1.model)
        self.assertIsNotNone(self.auto1.year)
        #Value mavjud emasligi - assertIsNone
        self.assertIsNone(self.auto1.price)
        #Value teng ekani - assertEquals
        self.assertEqual(0,self.auto1.get_km())

        #Let check second auto - auto2

    def test_set_price(self):
        new_price = 66000
        self.auto2.set_price(new_price)
        self.assertEqual(new_price,self.auto2.price)

    def test_add_km(self):
        #For value " + "
        self.auto1.add_km(self.km)
        self.assertEqual(self.km,self.auto1.get_km())
        self.auto1.add_km(5000)
        self.assertEqual(9000,self.auto1.get_km())

        #For value " - "
        new_km = -5000
        try:
            self.auto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            

unittest.main()