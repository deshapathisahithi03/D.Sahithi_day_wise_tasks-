import threading
import time

def thread_function(i):
    print(f"Thread {i} is running")

threads = []

# Create threads for each value in the range 10000 to 19999
for i in range(10000):
    thread = threading.Thread(target=thread_function, args=(i,))
    threads.append(thread)
    thread.start()
    time.sleep(0)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished.")



