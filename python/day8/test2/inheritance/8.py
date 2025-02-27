class Animal:
    def speak(self):
        print("animal sound")
        
class Dog(Animal):
    def speak(self):
        print("Barks")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
    
d=Dog()
d.speak()
c=Cat()
c.speak()