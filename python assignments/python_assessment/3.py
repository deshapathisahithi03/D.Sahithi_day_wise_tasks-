from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area():
        pass
class Rectangle(Shape):
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area(self):
        print(f"the area of rectangle:{self.length*self.bredth}")
 
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"the area of rectangle:{3.14*self.radius**2}") 

r=Rectangle(25,78)
r.area()    

c=Circle(1)
c.area()
  
        
    