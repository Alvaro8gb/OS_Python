import threading
import time

def thread_function():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

thread2 = threading.Thread(target=thread_function)
thread2.daemon = True

thread2.start()
print("Main thread continuing...")


