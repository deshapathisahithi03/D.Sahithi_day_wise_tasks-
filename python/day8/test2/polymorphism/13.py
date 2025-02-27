class Shape:
    def area(self):
        print("the area of the shapes are caleculated")
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"the area of square is:{self.side ** 2}")

class Triangle(Shape):
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
        
    def area(self):
        print(f"the area is triangle:{1/2*self.length*self.bredth}")
        
s=Square(5)
s.area()
t=Triangle(6,8)
t.area()