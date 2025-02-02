from abc import ABC,abstractmethod

class Animal(ABC):

    def make_sound(self):
        pass
        
class Dog(Animal):
    def make_sound(self):
        print("Dog Bark")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow")
    
c=Cat()
c.make_sound()

d=Dog()
d.make_sound()
        
        
