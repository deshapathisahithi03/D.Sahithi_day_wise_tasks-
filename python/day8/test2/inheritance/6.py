class Vehicle:
    def display(self):
        print("this is a base class")
        
class Car(Vehicle):
    def display(self):
        super().display()
        print("Car is inherited from Vehicle")
        
class Bike(Vehicle):
    def display(self):
        super().display()
        print("Bike is inherited from Vehicle")
        
class ElectricCar(Car):
    def display(self):
        super().display()
        print("ElectricCar is inherited from Car")
        
c=Car()
c.display()
b=Bike()
b.display()
ec=ElectricCar()
ec.display()