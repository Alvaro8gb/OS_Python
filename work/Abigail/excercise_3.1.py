import pandas as pd
import threading
import time

def sequential_avg(df):
    start_time = time.time()
    avg_values = {}
    for col in df.columns:
        avg_values[col] = df[col].mean()
    end_time = time.time()
    total_time = end_time - start_time
    return avg_values, total_time

def thread_avg(df):
    def calculate_avg_column(df, col, results, times):
        start_time = time.time()
        avg = df[col].mean()
        end_time = time.time()
        results[col] = avg
        times[col] = end_time - start_time

    start_time = time.time()
    results = {}
    times = {}
    threads = []

    for col in df.columns:
        thread = threading.Thread(target=calculate_avg_column, args=(df, col, results, times))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    return results, times, total_time

if __name__ == "__main__":
    # Sample DataFrame
    data = {
        'A': [1, 2, 3,4,5,6,7,8,9,10],
        'B': [11,12,13,14,15,16,17,18,19,20],
        'C': [21,22,23,24,25,26,27,28,29,30]
    }
    df = pd.DataFrame(data)

    # Calculate average sequentially
    sequential_result, sequential_time = sequential_avg(df)

    # Calculate average using threads
    thread_result, thread_times, total_time = thread_avg(df)

    # Write results to Markdown file
    with open("thread_analysis.md", "w") as f:
        f.write("# Thread Analysis\n\n")
        f.write("## Sequential Approach\n\n")

        for col, avg in sequential_result.items():
            f.write(f"### Category: {col}\n\n")
            f.write(f"Average Value: {avg}\n\n")
            f.write(f"Execution Time: {sequential_time:.6f} seconds\n\n")

        f.write("## Threaded Approach\n\n")

        for col, time_taken in thread_times.items():
            f.write(f"### Category: {col}\n\n")
            f.write(f"Average Value: {thread_result[col]}\n\n")
            f.write(f"Execution Time: {time_taken:.6f} seconds\n\n")