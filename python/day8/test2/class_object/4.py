class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        
    def student_details(self):
        return self.name,self.roll_number
    
s=Student("Devi","54637A067")
s.student_details()
print("the student name is:",s.name)
print("the roll number is:",s.roll_number)

    