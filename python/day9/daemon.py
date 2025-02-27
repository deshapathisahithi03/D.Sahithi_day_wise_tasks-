import threading
import time
def daemon_test():
    while True:
        print("daemon thread roaming")
        time.sleep(10)
        
d=threading.Thread(target=daemon_test,daemon=True)
d.start()

time.sleep(1)
print("main thread exiting")