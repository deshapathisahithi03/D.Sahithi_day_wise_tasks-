class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def check_availability(self,quantity):
        if quantity<=self.stock:
            print(f"the quantity is available and stock available:{self.stock}")
            
        else:
            print(f"the quantity is less")
            
p=Product("Noodles",5000,100)
quantity=50
print(f"the product name is:{p.name}")
print(f"the price of the product:{p.price}")
p.check_availability(quantity)
    