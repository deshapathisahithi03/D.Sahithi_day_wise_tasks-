class Payment:
    def process_payment(self,amount):
        print(f"the {amount} is added to the account based on three methods")
        
class PaypalPayment(Payment):
    def process_payment(self, amount):
        print(f"the {amount} is added in paypal processing")
        
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"the {amount} is added in credit card processing")
        
class BitConPayment(Payment):
    def process_payment(self, amount):
        print(f"the {amount} is added in block chain  processing")
        
p1=PaypalPayment()
p1.process_payment("$100")
p2=CreditCardPayment()
p2.process_payment("800")
p3=BitConPayment()
p3.process_payment("500")