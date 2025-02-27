from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
        
    def calculate_area(self):
        super().calculate_area()
        print(f"the area of Rectangle:{self.length*self.bredth}")

class  Circle(IShape):
        def __init__(self,radius):
            self.radius=radius
        def calculate_area(self):
             super().calculate_area()
             print(f"the area of circle is:{3.14*self.radius**2}")
             
r=Rectangle(2,3)
c=Circle(3)
r.calculate_area()
c.calculate_area()