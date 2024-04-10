import pandas as pd
import threading
from time import time

data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)


def calculate_mean(df, result, lock, column):
    start_time = time()
    column_avg = df[column].mean()
    end_time = time()
    lock.acquire()
    try:
        result[column] = {'mean': column_avg, 'execution_time': end_time - start_time}
    finally:
        lock.release()

def calculate_mean_threaded(df, lock, result, columns, num_threads):
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=calculate_mean, args=(df, result, lock, columns[i]))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    num_threads = 3
    result = {}

    start = time()
    lock = threading.Lock()

    calculate_mean_threaded(df, lock, result, ['A', 'B', 'C'], num_threads)

    end = time()

    with open("thread_analysis.md", "w") as f:
        f.write("Thread Analysis\n")
        for key, value in result.items():
            f.write(f"{key}: Mean: {value['mean']}, Execution Time: {round(value['execution_time'], 8)}\n")
