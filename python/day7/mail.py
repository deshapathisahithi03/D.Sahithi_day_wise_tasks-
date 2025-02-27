from abc import ABC,abstractmethod
class Mail(ABC):
    @abstractmethod
    def send_mail(self):
        pass
    
class Email(Mail):
    def send_mail(self):
        print("the mail has successfully sent via email")

class SMS(Mail):
    def send_mail(self):
        print("the mail has successfully sent via SMS")
class Whatsapp(Mail):
    def send_mail(self):
        print("the mail has successfully sent via Whatsapp")
        
e=Email()
e.send_mail()

s=SMS()
s.send_mail()

w=Whatsapp()
w.send_mail()

            
    