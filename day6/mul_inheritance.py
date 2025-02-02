#inheritance-group of class belongs to one
#parent class
class Shape:
    def area(self):
        pass

#child class
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius ** 2
    
class Square(Shape):
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
        
    def areas(self):
        return self.length * self.bredth
    
c=Circle(5)
print(f"the are of circle is:{c.area()}")
sq=Square(2,3)
print(f"the area of square is:{sq.area()}")
        