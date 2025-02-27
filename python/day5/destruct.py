class DestructorExample:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
    def __del__(self):
        print(f"object {self.name} is destroyed")
    
#create and delete an object
obj = DestructorExample("Sample")
del obj