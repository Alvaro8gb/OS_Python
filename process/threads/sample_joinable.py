from threading import Thread
import time

def thread_function():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

thread1 = Thread(target=thread_function)
thread1.start()

thread1.join() # Parent wait 



