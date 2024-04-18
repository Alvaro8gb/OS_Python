# Calculate the sequential average of columns from a data frame.
# Utilize threads for the calculation.
# Compare the execution times.
# Report the results in a markdown file named "thread_analysis.md"

from sklearn import datasets # pip install scikit-learn
import pandas as pd # pip install pandas
import threading
import time
 
dataset = datasets.load_breast_cancer()
 
# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

# print(dataset.DESCR)

# print(dataset.feature_names)
# print(df['radius error'][0]) # Acces to row 0

df_numeric = df.select_dtypes(include=['number'])

# print(df_numeric.columns)

def calculate_sequential_avg(df):
    results = {}  # To store average results
    times = {}  # To store time taken by each thread
    
    threads = []
    for col in df.columns:
        thread = threading.Thread(target=measure_time, args=(df, col, results, times))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results, times

def measure_time(df, col, results, times):
    start_time = time.time()  # Start time measurement
    average = df[col].mean()  # Calculate average
    end_time = time.time()  # End time measurement
    results[col] = average
    times[col] = end_time - start_time
    # print("subtracted 1: ", times[col])

if __name__ == "__main__":
    average_results, execution_times = calculate_sequential_avg(df)
    
    with open("thread_analysis.md", "w") as file:
        file.write("# Thread Analysis Report\n")
        file.write("## Execution Time Comparison\n")

        for col in df.columns:
            # print("subtracted 2: ", execution_times[col])
            file.write(f"Column: {col}\n")
            file.write(f"Average: {average_results[col]:f}\n")
            file.write(f"Execution Time: {execution_times[col]:.4} seconds\n\n")

