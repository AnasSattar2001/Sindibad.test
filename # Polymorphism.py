# Polymorphism
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")

class ElectricCar(Car):
    def drive(self):
        print(f"The {self.make} {self.model} is driving silently.")

# Polymorphism
my_car = Car("Toyota", "Corolla", 2022)
my_electric_car = ElectricCar("Tesla", "Model S", 2023)

my_car.drive()
my_electric_car.drive()
