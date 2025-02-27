import threading#1
import time#2
print("Main thread started")
def single_task():
    print("sub task started")#4
    time.sleep(3)#5
    print("sub task completed")#6
def square(side):
    area=side*side
    time.sleep(3)
    print(f"the area of square:{area}")
    
thread=threading.Thread(target=single_task)#3
thread.start()#4
thread.join()#7#waiting for the thread to finish before exiting 

s=threading.Thread(target=square(5))
s.start()
s.join()
time.sleep(2)
    
print("main thread execution completed")#8