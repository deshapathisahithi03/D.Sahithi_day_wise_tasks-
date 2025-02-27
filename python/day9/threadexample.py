import threading
import time

print(f"main task is started to execute")
def factorial_p(n):
    print("sub task started")
    time.sleep(5)
    fact=1
    for i in range (2,n+1):
        fact=fact*i
    print(f"factorial is:{fact}")
    print("sub task has exceuted" )
        
f=threading.Thread(target=factorial_p,args=(5,))
f.start()
f.join()
time.sleep(3)
print("the main task execution completed")

        
    