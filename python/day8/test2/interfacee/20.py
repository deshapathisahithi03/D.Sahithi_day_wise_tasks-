import time
from abc import ABC, abstractmethod

# Interface UserAuthentication
class UserAuthentication(ABC):
    
    @abstractmethod
    def login(self, username, password):
        pass
    
    @abstractmethod
    def logout(self):
        pass


# Google Authentication Class implementing UserAuthentication
class GoogleAuth(UserAuthentication):
    
    def login(self, username, password):
        print(f"Logging in with Google account: {username}")
        # Code to authenticate the user with Google credentials
        # (Here we are just simulating login process)
        print(f"Google account '{username}' logged in successfully.")

    def logout(self):
        print("Logging out from Google account.")
        # Code to log the user out from Google
        print("Google account logged out successfully.")


# Facebook Authentication Class implementing UserAuthentication
class FacebookAuth(UserAuthentication):
    
    def login(self, username, password):
        print(f"Logging in with Facebook account: {username}")
        print(f"Facebook account '{username}' logged in successfully.")

    def logout(self):
        print("Logging out from Facebook account.")
        print("Facebook account logged out successfully.")


# Simulate logging in and out with Google
google_auth = GoogleAuth()
google_auth.login("abc@gmail.com", "password123")
google_auth.logout()
    
# Simulate logging in and out with Facebook
facebook_auth = FacebookAuth()
facebook_auth.login("abc_facebook.com", "password123657")
time.sleep(5)
facebook_auth.logout()
