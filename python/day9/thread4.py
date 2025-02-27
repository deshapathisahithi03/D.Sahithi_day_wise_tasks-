import threading
import time
def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the lock")
        
lock=threading.Lock()
t=threading.Thread(target=task, args=(lock,))
t.start()
t.join()
print("the main thread as completed")