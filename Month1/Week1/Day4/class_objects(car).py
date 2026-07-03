#1. Create a Car class with attributes (brand, model, year) and a method that displays the car’s info
class Car:
    def __init__(self, brand, model, year):
        self.brand= brand
        self.model= model
        self.year= year

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

car1= Car("Toyota", "Corolla Grande", 2018)
car1.display_info()