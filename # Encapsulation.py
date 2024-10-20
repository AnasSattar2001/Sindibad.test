# Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self._year = year  # Encapsulation
    
    def get_year(self):
        return self._year
    
    def set_year(self, year):
        if year > 1885:  # Encapsulation
            self._year = year
        else:
            print("Invalid year for a car.")
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.get_year()}")

# Encapsulation
my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info()
my_car.set_year(2025)
my_car.display_info()
