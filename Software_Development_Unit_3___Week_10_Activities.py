carInfo = {'car01':['toyota', 4, 'gas', 'red']}

class Truck: 
    def __init__(self, make, num_wheels, fuel_type, color):
        self.make = make
        self.num_wheels = num_wheels
        self.fuel_type = fuel_type
        self.color = color

    def set_num_wheels(self, num_wheels):
        self.num_wheels = num_wheels

    def get_num_wheels(self):
        return self.num_wheels

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"The brand of the car is {self.make}, the car has {self.num_wheels} wheels, the color is {self.color}, and the fuel type is {self.fuel_type}."

'''
    def set_num_wheels(self, num_wheels):
        self.num_wheels = num_wheels

    def get_num_wheels(self):
        return self.num_wheels

    def set_fuel_capacity(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def get_num_wheels(self):
        return self.fuel_capacity

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def get_fuel_type(self):
        return self.fuel_type

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color'''
    




car01 = Truck('toyota', 0, 'gas', 'none')

car01.set_num_wheels(4)
car01.set_color('red')

print(car01)