from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        print(f"sum:{self.a+self.b}")
        
    def subtract(self):
        print(f"difference:{self.a-self.b}")
    
    def multiply(self):
        print(f"multiply:{self.a*self.b}")
        
    def divide(self):
        print(f"divide:{self.a/self.b}")
        
b=BasicCalculator(5,4)
b.add()
b.subtract()
b.multiply()
b.divide()
        