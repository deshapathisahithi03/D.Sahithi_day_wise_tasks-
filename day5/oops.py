#oops
#class:reusability of variables ex:exams marks,data entry already stored to access,setting the boundary for new datatype creation.
# member variable+member function.
#object:class is a define we create a cycle is object.
#rules fo class
#self----keyword to use inside class***it is the interpreter between  caller and class
#init-constructor:creates a object for a class and in this we can call directly
#dictionary is a another class
#constructor is used to create an instance of an object
#set-set the value when the functions are in private
#get-get the value when the functions are in private

#sample
'''class Movie:
    def __init__(self,director,hero):
        self.director=director#assigning the value to it
        self.hero=hero
    def displays(self):
        print(f"movies's :{self.director} {self.hero}:")
movie1=Movie("Anil","F2")
movie2=Movie("Jakanna","RRR")
movie3=Movie("Shankar","Robo")
movie1.displays()
movie2.displays()'''
'''class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    
    def set_salary(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
    def calculate_net_sal(self,allowance,deduction):
        net_salary=self._salary+allowance-deduction
        return net_salary
        
        
    
emp=Employee("alice",5000)
print("salary before update:",emp.get_salary())
n=int(input("enter salary:"))
emp.set_salary(n)
print("salary after update :",emp.get_salary())  

allowance=int(input("enter allowance "))
deduction=int(input("enter deduction"))
net_salary=emp.calculate_net_sal(allowance,deduction)
print(f"the salary after getting allowance and deduction:{net_salary}")'''

'''#inheritance
class Parent:
    def __init__(self):
        self.bignose="7cm"
    def display_parent(self):
        print("this is the parent class")
class Child(Parent):
    def __init__(self):
#blueprint of the parent is called into the super()
        super(). __init__()#constructor of parent class is called in child class
    def display_child(self):
        print("this is a child class")
        
child=Child()
child.display_child()
child.display_parent()
print(child.bignose)'''

#example:logging into an account and log off from the account(can navigate the time for exit and entry)

'''class School:
        def __init__(self):
            self.school_name="vgs"
        def display_school(self):
            print(f"the school is parent class")
            
class College(School):
        def __init__(self):
            super().__init__()
        def display_pg_college(self):
            print("the school is converted into pg college")
        def display_ug_college(self):
            print("the school is converted into ug college")
        
college=College()
college.display_school()
college.display_pg_college()
college.display_ug_college()
print(college.school_name)'''
        
'''class School:
    def __init__(self, student_name, age, marks):
        self._student_name = student_name
        self._age = age
        self._marks = marks

    def set_student_details(self, student_name, age, marks):
        self._student_name = student_name
        self._age = age
        self._marks = marks

    def get_student_details(self):
        return (self._student_name, self._age, self._marks)


class College(School):  # Inherits from School
    def __init__(self, student_name, age, marks, department):
        super().__init__(student_name, age, marks)  # Call the parent constructor
        self._department = department  # New attribute specific to College

    def set_department(self, department):
        self._department = department

    def get_department(self):
        return self._department

    def get_student_details(self):
        details = super().get_student_details()
        return details + (self._department,)  # Include department in details


# Example Usage
student = College("Sahithi", 20, 85, "Computer Science")
print("Student Details:", student.get_student_details())

student.set_student_details("Bob", 22, 90)
student.set_department("Computer Science Engineering")
print("Updated Student Details:", student.get_student_details())'''

class School:
    def __init__(self, school_name, student_name, age, marks):
        self.school_name = school_name
        self.student_name = student_name
        self.age = age
        self.marks = marks
    def display_school(self):
        print(f"School Name:{self.school_name}")
        print(f"Student Name:{self.student_name}")
        print(f"Age:{self.age}")
        print(f"Marks Obtained:{self.marks}")

class College(School):
    def __init__(self, school_name, student_name, age, marks, ug_department):
        super().__init__(school_name, student_name, age, marks)
        self.ug_department = ug_department
    def display_ug_college(self):
        print(f"Student Name:{self.student_name}")
        print(f"UG Department:{self.ug_department}")
    def display_pg_college(self, pg_course):
        print(f"Student Name:{self.student_name}")
        print(f"PG Course: {pg_course}")
        
school_name = input("Enter the School Name: ")
student_name = input("Enter the Student Name: ")
age = int(input("Enter the Student's Age: "))
marks = float(input("Enter the Marks Obtained in School: "))
ug_department = input("Enter the UG Department: ")
pg_course = input("Enter the PG course: ")

college = College(school_name, student_name, age, marks, ug_department)
college.display_school()
college.display_ug_college()
college.display_pg_college(pg_course)



            