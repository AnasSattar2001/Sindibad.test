# Methods
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine started.")
    
    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine stopped.")

# إMethods
my_car = Car("Toyota", "Corolla", 2022)
my_car.start_engine()
my_car.stop_engine()
