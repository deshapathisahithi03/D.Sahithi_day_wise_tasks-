#we use 'ABC' (abstract base class) and '@abstractmethod' to define an interface
#every method should be implemented and given to interface
#concept that defines a contract for classes to follow. It specifies what methods a class should implement, but not how they should be implemented.
from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    
class Child():
    def disp(self):
        print("child class")
        print("defining abstract method")
        
c=Child()
c.disp()   