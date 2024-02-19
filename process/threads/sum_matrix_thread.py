import threading
import random

MATRIX_SIZE = 1000
NUM_THREADS = 4

matrix = [[random.randint(0, 9) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
total_sum = 0
sum_mutex = threading.Lock()

def thread_sum(thread_id):
    global total_sum

    local_sum = 0

    # Sum the elements in the section assigned to the thread
    start = thread_id * MATRIX_SIZE // NUM_THREADS
    end = (thread_id + 1) * MATRIX_SIZE // NUM_THREADS

    for i in range(start, end):
        for j in range(MATRIX_SIZE):
            local_sum += matrix[i][j]

    # Add the local sum to the total sum, protecting with a mutex
    with sum_mutex:
        total_sum += local_sum

def main():
    threads = []
    thread_ids = list(range(NUM_THREADS))

    # Create threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=thread_sum, args=(thread_ids[i],))
        threads.append(thread)
        thread.start()

    # Wait for threads to finish
    for thread in threads:
        thread.join()

    # Print the total sum
    print("The total sum of the matrix is:", total_sum)

if __name__ == "__main__":
    main()
