import threading
import sys
from time import time


total = 0

def calculate_sum(start, end, numbers, lock):
    global total
    partial_sum = sum(numbers[start:end])
    
    # Acquire the lock before updating the shared variable
    lock.acquire()
    try:
        total += partial_sum
    finally:
        # Release the lock to allow other threads to acquire it
        lock.release()

def sum_with_threads(numbers, lock, num_threads):
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=calculate_sum, args=(i * len(numbers) // num_threads, 
                                                             (i + 1) * len(numbers) // num_threads, 
                                                             numbers, lock))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_threads = int(sys.argv[1])
    num_elems = int(sys.argv[2])
    
    numbers = list(range(1, num_elems))
    print("Number of elements", len(numbers))

    # Shared variable 'total' and a lock for synchronization
    start = time()
    lock = threading.Lock()
    
    sum_with_threads(numbers, lock, num_threads)

    end = time()

    print("Time execution", end-start, "Total", total)