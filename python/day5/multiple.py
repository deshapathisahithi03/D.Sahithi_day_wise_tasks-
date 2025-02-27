# Parent class 1
class Man:
    def __init__(self, man_name):
        self.man_name = man_name  # Initialize with man_name

    def walk(self):
        return "The man can walk."

# Parent class 2
class Woman:
    def free_bus(self):
        return "The woman will travel in a free bus."

# Child class inheriting from both Man and Woman
class Person(Man, Woman):
    def __init__(self, man_name,age):
        Man.__init__(self, man_name,age)  # Man's constructor
        self.age=age
    def friends(self):
        return "Both are friends."

# Create an object of Person 
person = Person("sahithi",22)  # Pass the name to the constructor

# Call methods
print(person.walk())  # Inherited from Man
print(person.free_bus())  # Inherited from Woman
print(person.friends())  # Method from Person

#  to create a Man object with a name
m1 = Man("John")  # Pass 'John' as the name
print(f"{m1.man_name} can walk: {m1.walk()}")
