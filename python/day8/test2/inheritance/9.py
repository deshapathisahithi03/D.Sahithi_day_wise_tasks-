class Car:
    def move(self):
        print("the car goes on the road")
        
class Airplane:
    def move(self):
        print("the airplane fly in the air")
        
class FlyingCar(Car,Airplane):
        def move(self):
            super().move()
            Airplane.move(self)
    
f=FlyingCar()
f.move()