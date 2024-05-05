import threading
import time
 
'''
Its malware be careful

'''
# Shared resource (example: a counter)
counter = 0
 
lock1 = threading.Lock()
lock2 = threading.Lock()
 
def thread1():
    global counter
    print("Thread 1: Acquiring lock1...")
    lock1.acquire()  # Acquire lock1
 
    print("Thread 1: Incrementing counter")
    counter += 1
 
    print("Thread 1: Waiting for lock2...")
    lock2.acquire()  # Attempt to acquire lock2 (hold for a while)
    print("Thread 1: Acquired lock2 (deadlock imminent)")
 
    # No exception handling here, deadlock occurs
 
    time.sleep(5)  # Simulate work for a few seconds
 
    # Locks are not released, deadlock persists
 
def thread2():
    global counter

    print("Thread 2: Acquiring lock2...")
    lock2.acquire()  # Acquire lock2
 
    print("Thread 2: Decrementing counter")
    counter -= 1
 
    print("Thread 2: Waiting for lock1...")
    lock1.acquire()  # Attempt to acquire lock1 (hold for a while)
    print("Thread 2: Acquired lock1 (deadlock imminent)")
  
    time.sleep(5)  # Simulate work for a few seconds
 
    # Locks are not released, deadlock persists
 
# Create threads
thread1 = threading.Thread(target=thread1)
thread2 = threading.Thread(target=thread2)
 
# Start threads
thread1.start()
thread2.start()
 
# Wait for threads to "finish" (effectively deadlocked)
thread1.join()  
thread2.join()  