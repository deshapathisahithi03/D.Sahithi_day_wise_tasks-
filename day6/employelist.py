#employee details are printed in the form of list
class Employee:
    def __init__(self,emp_id,emp_name,salary,age):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.salary=salary
        self.age=age
    def get_info(self,List1):
        List1= [self.emp_id,self.emp_name,self.salary,self.age]
        print("the list of employee:",List1)
List1=[]
emp_id=int(input("enter id:"))
emp_name=input("enter name:")
salary=int(input("enter salary:"))
age=int(input("enter age:"))
emp=Employee(emp_id,emp_name,salary,age)
emp.get_info(List1)


