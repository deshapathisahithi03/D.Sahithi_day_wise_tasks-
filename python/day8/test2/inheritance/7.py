class Person:
    def display(self):
        print("it is a parent class")
        
class Employee(Person):
    def display(self):
        super().display()
        print("employee is inherited from person")
        
class Manager(Employee):
    def approve_leave(self):
        super().display()
        print("the leave approval is successful")
        
e=Employee()
e.display()
m=Manager()
m.display()
m.approve_leave()