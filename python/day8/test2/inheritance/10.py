class Electronics:
    def __init__(self,brand):
        self.brand=brand
    def work(self):
        print("works good")
        
class MobileDevice(Electronics):
    def work(self):
        super().work()
        print(f"the type brand is:{self.brand}")
        
class SmartPhone(MobileDevice):
    def work(self):
        super().work()
        print(f"the brand of the smart phone:{self.brand}")
        
s=SmartPhone("Vivo")
s.work()
        
