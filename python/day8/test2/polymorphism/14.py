class Notification:
    def send(self):
        print(f"the notification is can send different ways ")
        
class EmailNotification(Notification):
    def send(self):
        print(f"the notification through email notification ")
        
class SMSNotification(Notification):
    def send(self):
        print(f"the notification is through SMSNotification")
        
e=EmailNotification()
e.send()
s=SMSNotification()
s.send()