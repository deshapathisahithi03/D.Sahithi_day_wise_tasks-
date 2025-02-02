from abc import ABC,abstractmethod

class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    @abstractmethod
    def max_speed():
        pass
    
class Car(Vehicle):
    def display(self,brand):
        print(f"the brand of the car is:{self.brand}")
    def max_speed(self):
        print(f"the maximum speed is 200km/h")
        
class Bike(Vehicle):
    def display(self,brand):
        print(f"the brand of the bike is:{self.brand}")
    def max_speed(self):
        print(f"the maximum speed is 150km/h")

brand1=input("enter brand name:")
c=Car(brand1)
c.display(brand1)
c.max_speed()

brand2=input("enter brand name:")
b=Bike(brand2)
b.display(brand2)
b.max_speed()
