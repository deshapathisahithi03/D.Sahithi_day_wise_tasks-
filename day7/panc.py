from abc import ABC,abstractmethod

class Father:
    def __init__(self,father_pan):
        self.father_pan=father_pan
        
    @abstractmethod
    
    def display(self):
        pass
    
    def show(self):
        print(f"the pan card number of father:{self.father_pan}")
        
class Child(Father):
    def __init__(self,father_pan,child_pan):
        super().__init__(father_pan)
        self.child_Pan=child_pan
        
    def display(self):
        print(f"the pan card number of child:{self.child_Pan} ")

father_pan=input("enter father pan number ")
child_pan=input("enter mother pan number 2")        
c=Child(father_pan,child_pan)
c.display()
c.show()
    
    