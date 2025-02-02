#a class derived ABC class which belongs to abc module.
#prebuilt functions are given to the class which is used by abstract class without doing overriding'
#from abc import ABC,abstractmethod
# class Father(ABC):
#     @abstractmethod
#     def display(self):
#     pass
#     -------------Abstract Method without Body--not implemented
#     def show(self):
#         print(f"concrete")
#         -------------Concrete method/method with body-
from abc import ABC,abstractmethod
class Father(ABC):
        @abstractmethod
        def display(self):
            pass
        
        def show(self):
            print("concrete method")
class Child(Father):
    def display(self):
        print("Child is implementing the abstract method")
    
class Mother(Father):
    def display(self):
        print("Mother is implementing than abstract class")
    
    
c=Child()
c.display()
c.show()

m=Mother()
c.display()
c.show()