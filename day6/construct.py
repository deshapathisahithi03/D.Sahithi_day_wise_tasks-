# *args - we can define multiple parameters-(*)
#[*args]
# a[**kwargs]-in this named argument comes with 2 stars,when we give input from outside it will not take,it will work within that constructor
'''class Example:
    def __init__(self,name):#constructor 1
        print(f"the constructor as hello {name}")
    def __init__(self,age):#constructor 2
        print(f"the constructor as age:{age}")

#creating an object
obj=Example(30) #calls only second constructor
#class is overridden
class Example:
        def __init__(self,*args):
            if len(args)==1:
                print(F"hello {args[0]}")
            elif len(args)==0:
                print(f"hello {args[0]},you are {args[1]} years old")

obj1=Example("dhana")

class Example:
    def __init__(self,student_name,**kwargs):
        self.student_name=student_name
        if "name" in kwargs and "age" in kwargs:
            print(f"hello {kwargs['name']},you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(F"hello {kwargs['name']}")
        self.xfield=kwargs['name']
          
#creating objects
obj1=Example(name="dhana")
obj2=Example(age=52)
print(obj1.name)
print(obj1.xfield)'''
class Example:
    def __init__(self,name):#constructor 1
        print(f"the constructor as hello {name}")
    def __init__(self,age):#constructor 2
        print(f"the constructor as age:{age}")

# Example class handling *args
class Example:
    def __init__(self, *args):
        if len(args) == 1:
            print(f"Hello {args[0]}")
        elif len(args) == 2:
            print(f"Hello {args[0]}, you are {args[1]} years old")
        else:
            print("Invalid number of arguments")

# Creating objects
obj1 = Example("Dhana")  
obj2 = Example("Alice", 25)  
obj3 = Example()  


# Example class handling **kwargs
class Example:
    def __init__(self, student_name, **kwargs):
        self.student_name = student_name
        self.xfield = kwargs.get("name", "Default Name")  # Safe retrieval

        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")

# Creating objects with correct arguments
obj4 = Example("Student1", name="Dhana", age=30) 
obj5 = Example("Student2", name="Alice") 
obj6 = Example("Student3") 

# Accessing attributes safely
print(f"xfield value for obj4: {obj4.xfield}")  
print(f"xfield value for obj5: {obj5.xfield}")  
print(f"xfield value for obj6: {obj6.xfield}")  

