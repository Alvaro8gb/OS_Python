
import pandas as pd
import numpy as np
from sklearn import datasets
import threading
import time
import matplotlib.pyplot as plt


def main():

    # Load the breast cancer dataset and convert it to a Pandas DataFrame
    dataset = datasets.load_breast_cancer()
    df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
    df['target'] = dataset.target

    # Print the feature names and the first value of the 'radius error' column
    print("All Dataset Features:")
    print(dataset.feature_names)
    print(f"Value Example - Radius Error Element 1: {df['radius error'][0]}")

    # Print the numeric feature names
    print("Dataset Numeric Features:")
    df_numeric = df.select_dtypes(include=['number'])
    print(df_numeric.columns)

    # Sequentially calculate the average for each column in the data frame
    start_time = time.time()
    sequential_results = sequential_averages(df_numeric)
    sequential_mean = np.mean(np.array(list(sequential_results.values())))
    sequential_time = time.time() - start_time

    # Parallelly calculate the average for each column in the data frame
    start_time = time.time()
    threading_results = threading_averages(df_numeric, 4)
    threading_mean = np.mean(np.array(list(threading_results.values())))
    threading_time = time.time() - start_time

    # Print the results
    mean_comparison = ""
    if sequential_mean == threading_mean:
        mean_comparison = f"Overall value means are equal! ({sequential_mean})"
    else:
        mean_comparison = f"Overall value means are different! ({sequential_mean} vs {threading_mean})"
    print(mean_comparison)
    print(f"Sequential Execution Time: {sequential_time}s")
    print(f"Threading Execution Time: {threading_time}s")
    difference = sequential_time - threading_time
    print(f"Difference in Execution Times: {difference}s")
    average_time = (sequential_time + threading_time) / 2
    print(f"Average Execution Time: {average_time}s")

    # Plot the results in a bar graph and save it to a file
    plt.figure(figsize=(8, 4))
    plt.bar(['Sequential', 'Average', 'Threading'], [sequential_time, average_time, threading_time])
    plt.title('Execution Time Comparison')
    plt.xlabel('Execution Method')
    plt.ylabel('Execution Time (s)')
    plt.savefig('BAR_GRAPH_exercise_3.1.png')
    plt.close()

    # Determine the fastest and slowest method
    fastest_method = ""
    slowest_method = ""
    if difference < 0:
        fastest_method = "Sequential"
        slowest_method = "Threading"
    else:
        fastest_method = "Threading"
        slowest_method = "Sequential"

    # Report the results in a markdown file
    text = f"""
# Thread Analysis

## Calculation Confirmation
{mean_comparison}

## Execution Times
- Sequential: {sequential_time} seconds
- Threading: {threading_time} seconds 
- Average: {average_time} seconds

## Bar Graph
![EXERCISE 3.1 BAR GRAPH](BAR_GRAPH_exercise_3.1.png)

## Conclusion
The {fastest_method} method is faster than the {slowest_method} method by {abs(difference)} seconds.
"""

    # Open a new file in write mode
    with open('exercise_3.1_thread_analysis.md', 'w') as file:
        file.write(text)


def sequential_averages(data):

    # Function that calculates the average of the given column
    def calculate_column_average(vals, col):
        return vals[col].mean()

    # Calculate the average of all columns sequentially
    results = {}
    for column in data.columns:
        results[column] = calculate_column_average(data, column)
    return results


def threading_averages(data, num_threads):

    # Split the columns into equal parts for each thread
    threads = []
    columns_per_thread = np.array_split(data.columns, num_threads)
    thread_results = [{} for _ in range(num_threads)]

    # Function that calculates the average of all columns for each thread
    def calculate_column_average(index, cols):
        results = {}
        for col in cols:
            results[col] = data[col].mean()
        thread_results[index] = results

    # Create and start threads
    for i, columns in enumerate(columns_per_thread):
        thread = threading.Thread(target=calculate_column_average, args=(i, columns))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Combine results from all threads using the pipe operator
    combined_results = {}
    for result in thread_results:
        combined_results = combined_results | result
    return combined_results


if __name__ == '__main__':
    main()
