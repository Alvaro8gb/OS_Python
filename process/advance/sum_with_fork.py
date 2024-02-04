import os
import multiprocessing

def calculate_sum(start, end, numbers, total, lock):
    partial_sum = sum(numbers[start:end])
    
    # Acquire the lock before updating the shared variable
    lock.acquire()
    try:
        total.value += partial_sum
    finally:
        # Release the lock to allow other processes to acquire it
        lock.release()

def sum_with_fork(numbers, total, lock):
    num_processes = 4
    processes = []

    for i in range(num_processes):
        pid = os.fork()

        if pid == 0:
            # Child process
            start = i * len(numbers) // num_processes
            end = (i + 1) * len(numbers) // num_processes
            calculate_sum(start, end, numbers, total, lock)
            exit(0)

        elif pid > 0:
            # Parent process
            processes.append(pid)

    # Wait for all child processes to finish
    for pid in processes:
        os.waitpid(pid, 0)

if __name__ == "__main__":
    numbers = list(range(1, 10001))

    # Shared variable 'total' and a lock for synchronization
    total = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    sum_with_fork(numbers, total, lock)

    print("Sum using fork with lock:", total.value)
