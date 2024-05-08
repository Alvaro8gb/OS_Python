import pandas as pd
import threading
import time
from sklearn import datasets

avg_values = []

# takes the mean of all columns
def sequential_avg(df):
    start_time = time.time()
    avg_values = df.mean(axis=0) # 0 is columns, 1 is rows
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Sequential Execution Time: {execution_time} seconds")
    return avg_values


def avg_thread(start_index, chunk_size):
    avg_values.append(df.iloc[start_index:start_index + chunk_size].mean(axis=0)) 
    #iloc cuts the dataframe into a smaller chunk before the thread takes the mean


def threaded_avg(df, num_threads):
    start_time = time.time()
    chunk_size = len(df) // num_threads
    threads = []


    for i in range(num_threads):
        thread = threading.Thread(target=avg_thread, args=(i * chunk_size, chunk_size))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    avg_result = pd.DataFrame(avg_values).mean(axis=0)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Threaded Execution Time ({num_threads} threads): {execution_time} seconds")
    return avg_result




if __name__ == "__main__":
    dataset = datasets.load_breast_cancer()
    df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
    
    df_numeric = df.select_dtypes(include=['number'])

    print("Sequential Average:")
    seq_avg = sequential_avg(df_numeric)
    print("\nThreaded Average:")
    num_threads = 4
    threaded_avg_result = threaded_avg(df_numeric, num_threads)
