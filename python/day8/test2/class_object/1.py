class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    
    def display(self):
        print(f"Employee name:{self.name}")
        print(f"Employee id:{self.id}")
        print(f"Employee department:{self.department}")
   
name=input("enter name:")
id=input("enter id:")
department=input("enter department:")     
emp=Employee(name,id,department)
emp.display()
        