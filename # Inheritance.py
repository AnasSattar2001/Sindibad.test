# Inheritance
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def charge_battery(self):
        print(f"The {self.make} {self.model}'s battery is now fully charged.")

# Inheritance
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
my_electric_car.display_info()
my_electric_car.charge_battery()
