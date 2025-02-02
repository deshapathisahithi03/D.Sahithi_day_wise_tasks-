#default constructor
#parameterized constructor self.greet()-used in log application
#polymorphism-allows same method name to behave differently based in the object
'''class Cat:
        def sound(self):
            print("Meow")
class Dog:
        def sound(self):
            print("bark")

for animal in [Cat(),Dog()]:
    animal.sound()'''
    
class Car:
    def brand(self):
        print("BMW")
class Bus:
    def brand(self):
        print("Express")
        
for vehicles in [Car(),Bus()]:
    vehicles.brand()