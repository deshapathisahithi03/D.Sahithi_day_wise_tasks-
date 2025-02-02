from abc import ABC, abstractmethod

class Father:
        @abstractmethod
        def profession(self):
         pass

        def introduce(self):
            self.profession()
        print("I am a father.")

class Engineer(Father):
    def profession(self):
        print("I am an Engineer.")

class Doctor(Father):
    def profession(self):
        print("I am a Doctor.")

e = Engineer()
e.profession()
e.introduce()
d = Doctor()
d.profession()
d.introduce()
